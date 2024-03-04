from typing import Union, List, Dict, Optional
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> Optional[int]:
        max_salary = max(
            int(job["max_salary"])
            for job in self.jobs_list
            if job.get("max_salary", "").isdigit()
        )
        return max_salary if max_salary is not None else None

    def get_min_salary(self) -> int:
        pass

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
