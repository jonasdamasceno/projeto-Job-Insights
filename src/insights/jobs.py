from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, encoding="utf-8",) as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.jobs_list.append(row)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        return list(set(job['job_type'] for job in self.jobs_list))

    def filter_by_multiple_criteria(
        self, jobs: List[dict], filters: dict
    ) -> List[dict]:
        if not isinstance(filters, dict):
            raise TypeError

        filtered_jobs = [
            job
            for job in jobs
            if all(job.get(key) == value for key, value in filters.items())
        ]
        return filtered_jobs
