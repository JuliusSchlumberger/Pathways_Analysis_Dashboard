def validate_and_store_data(input_id, stored_data, final_comment, final_style):
    """
    Helper function to validate and store input data.
    Returns the validation style and the updated stored data.
    """
    if stored_data.get(input_id, None) == None:
        validation_style = {'display': 'block'}
        final_comment = "Please fill in all required fields."
        final_style = {'display': 'inline', 'marginLeft': '0.5vw', 'color': '#d9534f'}
    else:
        validation_style = {'display': 'none'}
        # stored_data[input_id] = None

    return validation_style, stored_data, final_comment, final_style