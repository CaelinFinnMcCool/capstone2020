import pytest
from c20_server.job_manager import JobManager
from c20_server.job import Job
from c20_server.user import User


@pytest.fixture(name='job_manager')
def make_job_manager():
    return JobManager()


def test_new_instance_is_empty(job_manager):
    assert job_manager.num_assigned() == 0
    assert job_manager.num_unassigned() == 0


def test_when_job_added_it_goes_into_unassigned(job_manager):
    job_manager.add_job(Job(1))

    assert job_manager.num_assigned() == 0
    assert job_manager.num_unassigned() == 1
    j = job_manager.request_job(User(100))
    assert j.job_id == 1


def test_when_job_requested_it_moves_to_assigned(job_manager):
    job_manager.add_job(Job(1))
    job_manager.request_job(User(100))
    assert job_manager.num_assigned() == 1
    assert job_manager.num_unassigned() == 0


def test_successful_job_is_removed_from_manager(job_manager):
    job_manager.add_job(Job(1))
    job_manager.request_job(User(100))
    job_manager.report_success(User(100))
    assert job_manager.num_assigned() == 0
    assert job_manager.num_unassigned() == 0


def test_failed_job_is_moved_back_to_unassigned(job_manager):
    job_manager.add_job(Job(1))
    job_manager.request_job(User(100))
    job_manager.report_failure(User(100))
    assert job_manager.num_assigned() == 0
    assert job_manager.num_unassigned() == 1


def test_adding_multiple_jobs_into_unassigned(job_manager):
    job_manager.add_job(Job(1))
    job_manager.add_job(Job(2))
    assert job_manager.num_assigned() == 0
    assert job_manager.num_unassigned() == 2


def test_multiple_jobs_move_to_assigned(job_manager):
    job_manager.add_job(Job(1))
    job_manager.add_job(Job(2))
    job_manager.request_job(User(100))
    job_manager.request_job(User(101))
    assert job_manager.num_assigned() == 2
    assert job_manager.num_unassigned() == 0


# stale job
