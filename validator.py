def check_step_sequence(df):
    df = df.copy()
    df['issue'] = ''

    # Define the ideal step order
    ideal_order = ['preparation', 'incubation', 'extraction', 'analysis']

    # Group by Sample_ID
    for sample_id, group in df.groupby('sample_id'):
        steps = list(group['step'].str.lower())
        detected_issues = []

        # Check for missing steps
        for expected_step in ideal_order:
            if expected_step not in steps:
                detected_issues.append(f'Missing: {expected_step}')

        # Check for out-of-order steps
        step_indices = [steps.index(s) for s in steps if s in ideal_order]
        if step_indices != sorted(step_indices):
            detected_issues.append('Out-of-order steps')

        # Apply issues back to DataFrame
        indices = group.index
        issue_str = '; '.join(detected_issues) if detected_issues else 'OK'
        for idx in indices:
            df.at[idx, 'issue'] = issue_str

    return df
