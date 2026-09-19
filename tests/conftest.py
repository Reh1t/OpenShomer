import pytest
import subprocess
from pathlib import Path

@pytest.fixture(autouse=True)
def restore_demo_agent():
    # Run the test
    yield
    # Restore the vulnerable agent directory after every test so mutations don't bleed
    subprocess.run(["git", "restore", "demo/vulnerable-agent"], check=False)
