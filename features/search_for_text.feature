Feature: Search for text
In order to find some information
As an unlogged user
I want to search for a phrase to get a list of possible helpful websites

    Background: Prepare a result page for future checks
        Given Browser is open on google main site
        When  User looks for a given phrase
        """
            Dummy Text
        """

    Scenario: Get website links as a result for text phrase
        Then Results page shows 10 website links

    Scenario: Result counter should be available
        Then Results page shows results counter

    Scenario: User has access to another page with result links
        When User opens next result page
        Then results are different than in the previous page
