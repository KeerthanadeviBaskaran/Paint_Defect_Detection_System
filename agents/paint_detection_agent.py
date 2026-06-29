def generate_report(predicted_class, skill, instructions, prompt):

    report = f"""
PAINT DEFECT ANALYSIS REPORT

Skill Used:
{skill}

Instructions Followed:
{instructions}

Prompt:
{prompt}

Detected Defect:
{predicted_class}

Conclusion:
The uploaded image belongs to the {predicted_class} defect category.
"""

    return report