from datetime import date

# Salsabilah-Empire-OS - HR Module Sandbox
# Inspired by Global Industrial Benchmarks (ACI Motors/Yamaha)

class SystemOperatorFilter:
    def __init__(self):
        self.min_deadline = date.fromisoformat("2026-05-30")
        self.required_capabilities = [
            "Quarterly Strategic Planning",
            "Monthly P&L Statement Monitoring",
            "Cash Flow Evaluation",
            "Institutional Sales Expansion"
        ]

    def evaluate_candidate(
        self,
        capabilities: list[str],
        segment_budget_experience: bool,
        submission_date: str
    ) -> dict:
        submitted = date.fromisoformat(submission_date)
        within_deadline = submitted <= self.min_deadline
        missing_caps = [
            cap for cap in self.required_capabilities if cap not in capabilities
        ]

        if segment_budget_experience and within_deadline and not missing_caps:
            return {
                "status": "STATUS: COMPLIANT - PROCEED TO SOVEREIGN COMMAND",
                "missing_capabilities": [],
                "deadline_met": True
            }

        return {
            "status": "STATUS: NON_COMPLIANT - FILTER NOISE",
            "missing_capabilities": missing_caps,
            "deadline_met": within_deadline
        }


# Initialize Sandbox Filter
operator_test = SystemOperatorFilter()

# Example Evaluation Run
sample_candidate = operator_test.evaluate_candidate(
    capabilities=[
        "Quarterly Strategic Planning",
        "Monthly P&L Statement Monitoring",
        "Cash Flow Evaluation",
        "Institutional Sales Expansion"
    ],
    segment_budget_experience=True,
    submission_date="2026-05-15"
)

print(sample_candidate)
