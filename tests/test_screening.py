from src.screening import screen_candidate
import warnings

def test_screen_candidate():
    resume = "Experienced backend developer with Python and AWS."
    jd = "Looking for a backend developer with Python experience and cloud deployment knowledge."

    result = screen_candidate(resume, jd)
    assert isinstance(result, str)
    assert len(result.strip()) > 0
