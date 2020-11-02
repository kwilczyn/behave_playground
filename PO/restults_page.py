from commons import web


class ResultsPage:

    result_link = "//div[@id='rso']//h3"
    results_counter = "//div[@id='result-stats']"
    next_page_button = "//table[@role='presentation']//a"

    @classmethod
    def get_all_result_links(cls):
        return web.find_elements(cls.result_link)

    @classmethod
    def count_all_result_links(cls):
        links = cls.get_all_result_links()
        return len(links)

    @classmethod
    def results_counter_should_be_visible(cls):
        web.wait_until_element_is_visible(cls.results_counter)

    @classmethod
    def show_next_result_page(cls):
        web.click_element(cls.next_page_button)
