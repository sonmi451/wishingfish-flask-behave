Feature: wishingfish page

    Scenario Outline: Homepage
        Given you are on the <homepage>
        Then the main content is displayed
        and the page title is displayed
        and the navigation panel is displayed

        Examples:
        | homepage          |
        | wishingfish.cards |

    Scenario Outline: Click shop link
        Given you are on the <homepage>
        When you click the shop link
        Then you are taken to the etsy shop

        Examples:
        | homepage          |
        | wishingfish.cards |

    Scenario Outline: Main content
        Given you are on the <homepage>
        Then the main content is displayed

        Examples:
        | homepage          |
        | wishingfish.cards |

    Scenario Outline: Main content refresh
        Given you are on the <homepage>
        Then the main content is displayed
        and you refresh the page
        and the main content shows a new image

        Examples:
        | seconds |
        | 5       |
        | 10      |
