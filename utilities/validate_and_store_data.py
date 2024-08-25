def validate_and_store_data(input_ids, values, stored_data):
    """
    Helper function to validate and store input data.
    Returns the validation style and the updated stored data.
    """
    validation_styles = []
    final_comment = "Your responses are saved. You can update your responses by re-submitting. Thank you!"
    final_style = {'display': 'inline', 'marginLeft': '0.5vw', 'color': '#5cb85c'}

    for input_id, value in zip(input_ids, values):
        if value is not None and value != '' and value != ' ':
            print(input_id, value)
            stored_data[input_id] = value

        if stored_data.get(input_id, None) == None:
            validation_style = {'display': 'block'}
            final_comment = "Please fill in all required fields."
            final_style = {'display': 'inline', 'marginLeft': '0.5vw', 'color': '#d9534f'}
        else:
            validation_style = {'display': 'none'}
        validation_styles.append(validation_style)
        # stored_data[input_id] = None
    print(stored_data)
    return validation_styles, stored_data, final_comment, final_style