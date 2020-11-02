Feature: Input value
As an unlogged user
I want to insert some value for further main page operations

    Background: Preparation of Main page
        Given Browser is open on google main site

    Scenario Outline: User is unable to set a value longer than 2048 characters
        When User provides <number> long value on the main page
        Then Only maximum number of characters has been written

       Examples: Left boundary values
       | number          |
       | 1               |
       | 2               |
       | 2048            |

       Examples: Right boundary values
       | number          |
       | 2049            |
       | 2050            |

    Scenario: User uses virtual keyboard to provide a value
        When User provides value using virtual keyboard
        Then given value is enabled in the searchbox