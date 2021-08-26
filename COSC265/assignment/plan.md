

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




# course
course_code_semester (eg COSC256-21S2)  :  KEY
course_name
description
dates
    start_date
    end_date
category
    id
    name
    owner (department, college, or unit) *Should this be a relationship instead?*

<course>  ==N=>  taught_by  <=N==  <lecturer>  
    ASSUME: each lecturer teaches at least 1 course.

<course> ==N=>  enrolled_in  <=N==  <student>
    +attribute:  mark
    +attribute:  grade  :  (derived from mark)
    ASSUME: each course has at least 1 student.)

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

<post> ==N=>  made_by_in  <--1-  <user>   :   IDENTIFYING RELATION   
<post> ==N=>  made_by_in  <--1-  <forum>  :  IDENTIFYING RELATION
    NOTE: use same diamond for both of these, maybe

<post> --1->  in_response_to <==1= <post>
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

<assignment> ==N=>  submitted_by  <--N- <student>
    ASSUME: at least one student submits an assignment
    +attributes:
        submission_time
            date
            time_of_day
        mark
        feedback




# quiz extends assessment

<quiz> ==N=> contains <=N==  <question>   :   IDENTIFYING
<quiz> --N-> submitted_by <-N-- <student>
    +attribute: mark   :   multivalued  (because students can attempt more than once)


# question
type
text
mark
penality_regime
ID   :   KEY within <quiz>





