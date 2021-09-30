

# user
id  :  KEY
password
name
    first
    last
profile_photo  :  optional  (dotted line to attribute)
biography  :  optional

# student extends user
student_number  :  KEY
start_year
hall_of_residence  :  optional

# teacher extends user
department_code
job_title


ASSUME that a user can be a teacher and a student at the same time.



# course
course_code_semester (eg COSC256-21S2)  :  KEY
course_name
description
dates
    start_date
    end_date

<course>  ==N=>  taught_by  <=N==  <lecturer>  
    ASSUME: each lecturer teaches at least 1 course.

<course> ==N=>  enrolled_in  <=N==  <student>
    +attribute:  mark
    +attribute:  grade  :  (derived from mark)
    ASSUME: each course has at least 1 student.)



# course_category
id
name
owner
ASSUME: id is unique within all courses



# course_section
section_number  :  KEY within <course>
title
description

<course_section> ==N=>  has_a  <==1= <course>   :  IDENTIFYING RELATIONSHIP



# resource
id  :  KEY within <course_section>
title
description
                      
<resource> ==N=>  has_a    <=1==    <course_section>   :  IDENTIFYING RELATION
    ASSUME: that every course section has at least one resource

# forum extends resource
post_privaleges  (i.e. who can post on forum)


<user> --N->  participate_in  <==N=  <forum>
    +attribute:  subscription_mode
    +derived_attribute:  can_post   (derived from user type, and forum.post_privaledges)
    (ASSUME: each forum has at least one user)



# post
topic
timestamp
text
ID  :  KEY within user AND within forum
    (NOTE: do one identifying relation, but TWO branches from same diamond.)

<post> ==N=>  MAKE_POST  <--1-  <user>   :   IDENTIFYING RELATION   
<post> ==N=>  MAKE_POST  <--1-  <forum>  :  IDENTIFYING RELATION
    NOTE: use same diamond for both of these, maybe
    (ASSUME: You need to be a registered user to post)
    (ASSUME: you cannot share posts across forums)


<post> --1->  in_response_to <--N- <post>
    ASSUME: it is not possible for a post to respond to itself
    ASSUME: you cannot reply to multiple posts at once.


# URL extends resource
web address

# file extends resource
filepath
display_option

# label extends resource
html_code
images  :  multivalue, optional



# assessment extends resource
total_worth


# assignment extends assessment
accepted_file_types  :  multivalue

<assignment> --N->  submitted_by  <--N- <student>
3 way:  <file> (0,N)
    +attributes:
        submission_time
            date
            time_of_day
        mark
        feedback
ASSUME: It's possible for the same file to be submitted twice, by different
    students. This would happen if the students try to cheat.




# quiz extends assessment

<quiz> ==N=> contains <=N==  <question>   :   IDENTIFYING
<quiz> --N-> submitted_by <-N-- <student>
    +attribute: mark   :   multivalued  (because students can attempt more than once)


# question
type
text
mark
penality_regime
ID   :   KEY
question_option   :  MULTIVALUED
    is_correct
    option_explanation
    candidate_answer

    ASSUME: questions IDs are not unique within questions.
        (it does not state that question IDs are key within questions.)
    ASSUME: questions can be shared across quizess, (for example, practice lab
            and real lab share the same question.)
    ASSUME: each question is in at least one quiz

student <select_options> question
    Attribute:
        student_submission
        is_correct   :  DERIVED (from student_submission and candidate_answer)

ASSUME that sometimes, quizzes and questions will not be submitted by any student.















