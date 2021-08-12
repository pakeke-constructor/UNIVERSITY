


Throughout our project planning phase, it is imperative to prepare for
things that could go wrong during the project.

The way we tackled this was by doing a risk assessment, and ranking the risks
based on the impact they would have, and the likelihood of them occuring.


<next_slide>



Here are a couple of the most prominent risks that we identified


- So, our most prominent risk was losing development time due to exam periods
    We agreed that this risk was the most prominent, because only does
    the responsibility of dealing with this risk lie amongst every
    member of the team, losing time due to exams is very real and has a
    high likelihood.

    <next_slide>

    So, how did we mitigate it?
    The way we have chosen to mitigate this is to incorporate deliverable freezes
    inbetween all the major exams, so that we aren't forced to work on multiple
    things at once.
    (You can see this in our milestone calender;
        orange is where exams are,
        green is where deliverable freezes are enacted)


<next_slide>

- The third most prominent risk we identified was scope creep.
    Now I believe we have talked about this before, but scope creep is basically
    when new features are added to the project when older, more important features
    are incomplete.

    A way of mitigating scope creep is to ensure that we stick to the project
    plan when developing, and do not pursue new features before primary
    features are fully complete, that is, the features that
    satisfy all the required quality and functional requirements.
    
    However, this isn't the whole story.
    Sometimes, we may be unsure whether a feature is beyond the scope or not.
    This was certainly the case with databases for us; we were unsure if we needed them.
    The biggest crime data CSV was 37 mb; that would easily fit in memory, however
    a database would be way more secure, so we weren't sure.

    A way of mitigating scope creep in this case, is thus to abstract
    away behaviour behind an API.

    <show dataManager classes>
    Here we can see the DataManager classes grouped together.

    By abstracting the data storage behind a class, it doesn't matter
    to the rest of the program whether data is stored in RAM or in a database.

    It can be easily changed in the future due to it's modularity, and
    potential scope creep becomes a lot easier to handle.


