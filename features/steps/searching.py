from behave import *
from PO.main_page import MainPage
from PO.restults_page import ResultsPage


@when("User looks for a given phrase")
def step_impl(context):
    MainPage.search_for_value(context.text)


@then("Results page shows {expected_number_of_links} website links")
def step_impl(context, expected_number_of_links):
    current_number_of_links = ResultsPage.count_all_result_links()
    assert int(expected_number_of_links) == current_number_of_links


@then("Results page shows results counter")
def step_imp(context):
    try:
        ResultsPage.results_counter_should_be_visible()
    except TimeoutError:
        raise AssertionError("Results counter is not visible!")


@when("User opens next result page")
def step_imp(context):
    context.first_site_links = ResultsPage.get_all_result_links()
    ResultsPage.show_next_result_page()


@then("results are different than in the previous page")
def step_imp(context):
    current_page_results = ResultsPage.get_all_result_links()
    assert context.first_site_links != current_page_results

