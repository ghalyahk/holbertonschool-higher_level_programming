import os

def generate_invitations(template, attendees):
    """
    Generates invitation files from a template and a list of attendee dictionaries.

    Args:
        template (str): The template string containing placeholders.
        attendees (list): List of dictionaries, each representing an attendee.

    Returns:
        None
    """

    # --- Input Type Validation ---
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__} instead.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees must be a list of dictionaries, got {type(attendees).__name__}.")
        return

    # --- Empty Input Checks ---
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # --- Process Each Attendee ---
    for idx, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values or "N/A" if missing or None
        invitation_text = template
        placeholders = ["name", "event_title", "event_date", "event_location"]

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation_text = invitation_text.replace(f"{{{key}}}", str(value))

        # --- Generate Output File ---
        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(invitation_text)
            # Optional: print confirmation
            # print(f"Generated {output_filename}")
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")
