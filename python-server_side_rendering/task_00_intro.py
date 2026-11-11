#!/usr/bin/python3
"""
Task 0: Creating a Simple Templating Program for Server-Side Rendering.
"""


class SafeMapping(dict):
    """Custom dictionary class to handle missing keys or None values as 'N/A'."""
    def __getitem__(self, key):
        val = super().get(key, "N/A")
        return val if val is not None and val != "" else "N/A"


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    """
    # 1. Validate input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # 2. Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # 3. Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 4. Process each attendee and generate output files
    for index, attendee in enumerate(attendees, start=1):
        filename = f"output_{index}.txt"

        # Format template using SafeMapping to handle missing keys/None values
        output_content = template.format_map(SafeMapping(attendee))

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(output_content)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")
