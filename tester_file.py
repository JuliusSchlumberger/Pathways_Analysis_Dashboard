import pandas as pd
import gzip
from waasmodel_v6.inputs_waasmodel import *
from waasmodel_v6.inputs_runclass import RunClassInputs

def calculate_robustnessvalues(data, optimization='default'):
    mean = robustness_mean(data)
    val10 = 0
    val90 = 0

    return [mean, val10, val90]

def robustness_mean(data, optimization='minimization'):
    mean = np.mean(data)
    out = np.round(mean, 2)
    return out

def calculate_costs(temp_inv, temp_maint, years_since_last_measure, measure_sequence,old_measures, sprink):
    # print(measure_sequence)
    if measure_sequence != 0:
        invest_inputs = pd.read_csv('waasmodel_v6/inputs/invest_costs.csv', index_col=0).values
        maint_inputs = pd.read_csv('waasmodel_v6/inputs/maint_costs.csv', index_col=0).values
        # maint_inputs = maint_inputs

        active_measures = measure_sequence.split('&')
        new_measure = active_measures[-1]
        # new_measure = [measure for measure in active_measures if measure not in old_measures]
        # print(measure_sequence,active_measures)
        old_measures = active_measures
        if new_measure != '':
            temp_inv += invest_inputs[int(float(new_measure)), int(float(new_measure))]

        for one_measure in active_measures[:-1]:
            if one_measure == 4: # 'd_riv_irrigation'
                sprink_years_since_last_measure = sprink[0][:years_since_last_measure]
                sprink[0] = sprink[0][years_since_last_measure:]
                temp_maint += years_since_last_measure * maint_inputs[
                    int(float(one_measure)), int(float(one_measure))] + sprink_years_since_last_measure * 1.03 / 10 * 1000000
            elif one_measure == 3: # 'd_gw_irrigation'
                sprink_years_since_last_measure = sprink[1][:years_since_last_measure]
                sprink[1] = sprink[1][years_since_last_measure:]
                temp_maint += years_since_last_measure * maint_inputs[
                    int(float(one_measure)), int(
                        float(one_measure))] + sprink_years_since_last_measure * 1.03 / 10 * 1000000
            elif one_measure == '':
                temp_maint = temp_maint
            else:
                temp_maint += years_since_last_measure * maint_inputs[
                    int(float(one_measure)), int(
                        float(one_measure))]

    return temp_inv, temp_maint, old_measures, sprink


def read_csv_file(file):
    # read the compressed file back into a DataFrame
    with gzip.open(file, 'rb') as f:
        df = pd.read_csv(f)
    return df



def calculate_100year_helper(file, cc_scenarios, stages, measure_dict, realization,
                             realization_numbers, realization_no, sector):
    # print(sector)
    df = read_csv_file(file=file)

    df[['fa_p', 'da_p', 'fu_p', 'ds_p']] = df.portfolio.str.split('_', expand=True)
    df[['fa_p', 'da_p', 'fu_p', 'ds_p']] = df[['fa_p', 'da_p', 'fu_p', 'ds_p']].astype(int)
    endvalue_list = []
    df_timing = []
    df_sector = df[df['sector_hazard'] == sector]


    for cc_scenario in cc_scenarios:
        df_cc = df_sector[df_sector['cc_scenario'] == cc_scenario]
        keys = df_cc.output.unique()
        keys_clean = [x for x in keys if not 'decision' in x or not 'sprink' in x]
        for key in keys_clean:
            df_key = df_cc[df_cc['output'] == key]

            for portfolio in df_key['portfolio'].unique():
                # print(sector, portfolio)
                df_portfolio = df_key[df_key['portfolio'] == portfolio]
                for climvar in df_portfolio['climvar'].unique():
                    df_climvar = df_portfolio[df_portfolio['climvar'] == climvar]
                    for reali in range(realization_no):
                        for measure in measure_dict[sector]:
                            df_real = df_climvar[
                                df_climvar['realization'] == realization + reali + realization_numbers[measure[0]]]
                            if 'pathway' in key:
                                # print(sector, portfolio, cc_scenario, climvar)
                                sectorname = key[-3:]
                                df_sprink_riv = df_real[df_real['output'] == 'sprink_riv']
                                # sprink_riv_sum = np.round(df_sprink_riv['value'].astype(float).sum(), 2)
                                df_sprink_gw = df_real[df_real['output'] == 'sprink_gw']
                                # sprink_gw_sum = np.round(df_sprink_gw['value'].astype(float).sum(), 2)
                                df_timing, endvalue_list = calculate_timings(df_real=df_real,
                                                                             endvalue_list=endvalue_list,
                                                                             df_timings=df_timing, stages=stages,
                                                                             sector=sector, cc_scenario=cc_scenario,
                                                                             climvar=climvar,
                                                                             portfolio=portfolio,
                                                                             real=realization + reali +
                                                                                  realization_numbers[
                                                                                      measure[0]],
                                                                             sectorname=sectorname, sprink=[df_sprink_riv, df_sprink_gw])
                                number_measures = df_real['value'].astype(str).str.split('&').str.len()
                                sum = number_measures.max() - 1
                                endvalue_list.append({
                                    'sum': sum,
                                    'output': key,
                                    'stage': stages[sector],
                                    'sector_hazard': sector,
                                    'cc_scenario': cc_scenario,
                                    'climvar': climvar,
                                    'portfolio': portfolio,
                                    'realization': realization + reali + realization_numbers[measure[0]],
                                })

                            else:
                                sum = np.round(df_real['value'].astype(float).sum(),2)
                                endvalue_list.append({
                                    'sum': sum,
                                    'output': key,
                                    'stage': stages[sector],
                                    'sector_hazard': sector,
                                    'cc_scenario': cc_scenario,
                                    'climvar': climvar,
                                    'portfolio': portfolio,
                                    'realization': realization + reali + realization_numbers[measure[0]],
                                })
    return pd.DataFrame(endvalue_list), pd.DataFrame(df_timing)


def get_100year_values_per_file(cc_scenarios, stages, sector, measure_dict, realization_numbers, realization,
                                realization_no, start_val, end_val, mainfolder, measure_realizations):
    unique_list = np.loadtxt(f'{mainfolder}/{str(realization).zfill(6)}/all_files_{sector}.txt', dtype=str,
                             delimiter=',')
    if end_val == -1:
        relevant_range = unique_list
    else:
        relevant_range = unique_list[start_val:end_val]

    tick = 0
    timeseries_output = f'{mainfolder}/{str(realization).zfill(6)}/stage_{stages[sector]}/timeseries_{sector}.csv'
    endvalues_output = f'{mainfolder}/{str(realization).zfill(6)}/stage_{stages[sector]}/endvalues_{sector}_{str(start_val)}_{str(end_val)}.csv'
    timing_output = f'{mainfolder}/{str(realization).zfill(6)}/stage_{stages[sector]}/timing_{sector}_{str(start_val)}_{str(end_val)}.csv'
    futures_timing = []
    futures_endvalues = []
    futures_timeseries = pd.DataFrame()

    for file in relevant_range:
        # print(tick, file)
        timeseries = make_timeseries(file=file)
        futures_timeseries = pd.concat([futures_timeseries, timeseries], ignore_index=True)

        endvalues, timings = calculate_100year_helper(file=file, cc_scenarios=cc_scenarios,
                                                      stages=stages, measure_dict=measure_dict,
                                                      realization=realization, realization_numbers=realization_numbers,
                                                      realization_no=realization_no, sector=sector)
        futures_timing.append(timings)
        futures_endvalues.append(endvalues)
        tick += 1
        if tick == 500 and len(relevant_range) > 500:
            timing = pd.concat(futures_timing)
            timing.to_csv(timing_output, index=False)
            endvalues = pd.concat(futures_endvalues)
            endvalues.to_csv(endvalues_output, index=False)
            futures_timing = []
            futures_endvalues = []
        if tick > 500 and tick % 500 == 0:
            timing = pd.concat(futures_timing)
            timing.to_csv(timing_output, mode='a', index=False, header=False)
            endvalues = pd.concat(futures_endvalues)
            endvalues.to_csv(endvalues_output, mode='a', index=False, header=False)
            futures_timing = []
            futures_endvalues = []
        if tick == len(relevant_range) and len(relevant_range) > 500:
            timing = pd.concat(futures_timing)
            timing.to_csv(timing_output, mode='a', index=False, header=False)
            endvalues = pd.concat(futures_endvalues)
            endvalues.to_csv(endvalues_output, mode='a', index=False, header=False)

        elif tick == len(relevant_range):
            timing = pd.concat(futures_timing)
            timing.to_csv(timing_output, index=False)
            endvalues = pd.concat(futures_endvalues)
            endvalues.to_csv(endvalues_output, index=False)

    futures_timeseries.to_csv(timeseries_output, index=False)


def create_robustness_df(df, cc_scenarios, sectors_list, stages):
    optimization = {'DamUrb_tot': 'min',
                    'DamAgr_f_tot': 'min',
                    'DamAgr_d_tot': 'min',
                    'DamShp_tot': 'min',
                    'invest_f_a': 'min',
                    'invest_f_u': 'min',
                    'invest_d_a': 'min',
                    'invest_d_s': 'min',
                    'invest_multihaz_agr': 'min',
                    'invest_multihaz_urb': 'min',
                    'invest_multihaz_multisec': 'min',
                    'maint_f_a': 'min',
                    'maint_f_u': 'min',
                    'maint_d_a': 'min',
                    'maint_d_s': 'min',
                    'maint_multihaz_agr': 'min',
                    'maint_multihaz_urb': 'min',
                    'maint_multihaz_multisec': 'min',
                    'revenue_agr': 'max',
                    'pathways_list_d_a': 'min',
                    'pathways_list_f_a': 'min',
                    'pathways_list_d_s': 'min',
                    'pathways_list_f_u': 'min'}

    robustness_list = []
    for cc_scenario in cc_scenarios:
        df_cc = df[df['cc_scenario'] == cc_scenario]
        for sector in sectors_list:
            df_sector = df_cc[df_cc['sector_hazard'] == sector]
            df_cc_stage = df_sector[df_sector['stage'] == stages[sector]]
            # keys = df_cc_stage.output.unique()
            # keys_clean = [x for x in keys if not x.startswith('pathway')]
            keys_clean = list(optimization.keys())
            # print(keys_clean)
            for key in keys_clean:
                df_key = df_cc_stage[df_cc_stage['output'] == key]
                for portfolio in df_key['portfolio'].unique():
                    df_portfolio = df_key[df_key['portfolio'] == portfolio]
                    # print(key, portfolio, sector)
                    mean, r_10, r_90 = calculate_robustnessvalues(data=df_portfolio['sum'].astype(float).values,
                                                                  optimization=optimization[key])
                    # robustness = call_function(func_name=robustness_type,data=df_portfolio['sum'].astype(float).values, optimization=self.optimization[key])

                    robustness_list.append({
                        'robustness': mean,
                        'r10': r_10,
                        'r90': r_90,
                        'output': key,
                        'stage': stages[sector],
                        'sector_hazard': sector,
                        'cc_scenario': cc_scenario,
                        'portfolio': portfolio,
                    })
    return pd.DataFrame(robustness_list)


def run_processing(mainfolder, endvalues, robustvalues, realization, sectors_list, start_val, end_val, no_realizations=1):
    runclass = RunClassInputs()
    keys_dict = runclass.keys_dict
    model_inputs = ModelInputs(stage=1)
    realization_numbers = model_inputs.measure_numbers

    stages = {'flood_agr': 1,
              'drought_agr': 1,
              'flood_urb': 1,
              'drought_shp': 1,
              'multihaz_agr': 2,
              'multihaz_urb': 2,
              'multihaz_multisec': 3
              }

    cc_scenarios = ['D', 'G', 'Wp']
    sectors = {1: ['flood_agr', 'drought_agr', 'flood_urb', 'drought_shp'],
               2: ['multihaz_agr', 'multihaz_urb'],
               3: ['multihaz_multisec']}
    measure_dict = {
        'flood_urb': [['no_measure']],
        'flood_agr': [['no_measure']],
        'drought_shp': [['no_measure']],
        'drought_agr': [['no_measure']],
        'multihaz_agr': [['no_measure']],
        'multihaz_urb': [['no_measure']],
        'multihaz_multisec': [['no_measure']]}
    if endvalues:
        for sector in sectors_list:
            get_100year_values_per_file(cc_scenarios=cc_scenarios, stages=stages,
                                        sector=sector, realization_no=no_realizations,
                                        measure_dict=measure_dict,
                                        realization_numbers=realization_numbers,
                                        realization=realization,
                                        start_val=start_val, end_val=end_val,
                                        mainfolder=mainfolder,
                                        measure_realizations=range(no_realizations))
    if robustvalues:
        for sector in sectors_list:
            endvalues_output = f'{mainfolder}/{str(realization).zfill(6)}/stage_{stages[sector]}/endvalues_{sector}_{str(start_val)}_{str(end_val)}.csv'
            robustness_output = f'{mainfolder}/{str(realization).zfill(6)}/stage_{stages[sector]}/robustness_{sector}_{str(start_val)}_{str(end_val)}.csv'
            endvalues_df = pd.read_csv(endvalues_output)
            robustness_df = create_robustness_df(df=endvalues_df, cc_scenarios=cc_scenarios, sectors_list=sectors_list, stages=stages)
            robustness_df.to_csv(robustness_output)

realization = 5000
sectors_list = ['flood_agr', 'drought_agr', 'flood_urb', 'drought_shp', 'multihaz_agr', 'multihaz_urb',
                'multihaz_multisec']
sectors_list = ['flood_agr']
mainfolder = 'model_outputs'
start_val = 0
end_val = -1

for sector in sectors_list:
    # Check completeness
    # run_checker(mainfolder=mainfolder, realization=realization,
    #             measure_realizations=[0], sector=sector)
    #
    # # create list of outputfiles
    # list_of_files(mainfolder=mainfolder,realization=realization, measure_realizations=[0],
    #                sector=sector)

    # create endvalues & robustness values
    run_processing(mainfolder='model_outputs', realization=realization, no_realizations=1,
                   sectors_list=sectors_list, start_val=start_val, end_val=end_val,
                   endvalues=True, robustvalues=True)