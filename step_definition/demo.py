from pytest_bdd import scenarios, given, when, then


@given("I open browser")
def step_impl(page):
    page.goto("https://example.com")
    assert False
