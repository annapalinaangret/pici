# Indicators

## Overview

The toolbox provides a repository of predefined indicators and simple tools to add new, custom indicators.

### Structure

By default, the central unit of observation is the forum **thread**, which can be part of one or multiple sub-forums. We propose that a thread is the *observable trace* of a sequence of interactions that can represent or display innovation activities. Each post in a thread is a **contribution** by a community member (the **contributor**). We single out the **initial contribution**, as we assume that XYZ. A **community** consists of a number of contributors and their contributions in threads, which are organized in sub-forums.

### Networks

Additional levels of observation are the **networks** formed by contributors. The two main representations are the *co-contribution network* and the *comment network*.

`co-contributor network`

: The co-contributor network is an *undirected graph* where each node represents a contributor. A pair of contributors is connected by an edge if both have contributed in at least one shared thread. The edge weight is proportional to the number of threads both contributed to.

`commenter network`

: The commenter network is a *directed graph* where each node represents a contributor. A contributor *A* has an edge pointing to contributor *B* if *A* has contributed in at least one thread where contributor *B* has posted the initial contribution (*A* has "commented"). The weight of edge *A*→*B* is proportional to the total number of comments *A* made on initial contributions of *B*.

<p align="center">
    <img src="../images/structure_and_terminology.png" width="700px" style="width: 55%; max-width:700px; min-width:300px;" />
</p>

### Levels of observation

Each indicator is observed on either **contributor**, **contribution**, **thread**, or **community** level. Aggregations of indicators are provided for higher levels. For example, the *number of contributions made by a contributor* can be an indicator for their role in the community. This indicator would be provided on thread-level as, e.g., *average number of contributions per contributor*, measured for all contributors that have contributed to a specific thread. Common aggregations are mean, sum, standard-deviation, min and max. Other aggregations (or *transformations*) could also pick out a single of multiple values. On thread-level, an example would be the *total number of contributions made by the contributor of the initial contribution*.

The thread observation level can be subdivided into three further subsets of posts: the whole thread, only the **initial contribution**, or only the **feedback** (all posts that were not authored by the initial contributor). This helps to implement indicators that rely on more detailed concepts, such as *ideas* in *idea communities*, or *questions* in *question communities*, which can potentially be operationalized by *inital contribution*.

[TODO: Grafik]

### Data

In order to be able to apply indicators to a heterogeneous set of communities, most indicators rely on the following basic data that can be collected from most online forums:

- contribution meta data: contributor, date, associated thread, position in thread, sub-forum
- contribution content: text, html, extracted links, images
- contributor properties: name/id
- thread: title

Other data, such as likes/upvotes, friendship-relations, contributor location, thread views, etc., might be available in some communities and can be included in more specialized indicators.

### List of indicators

The following list conceptually groups all available indicators. Each indicator description links to all relevant metrics that are implemented in the toolbox. Each indicator is labelled with its level of observation: <span class="label contributor">contributor</span> <span class="label contribution">contribution</span> <span class="label initial-contribution">initial contribution</span>
 <span class="label thread">thread</span> <span class="label community">community</span>. Specialized indicators are marked with <span class="label specialized">specialized</span> and state which additional data is required.

Please refer to the [user guide]() and the [examples]() on how to [generate the indicators]() or how to [implement a custom indicator]().

## Status and reputation

### In-degree centrality

- [``in-degree centrality``](../reference/pici/metrics/network/#pici.metrics.network.in_degree_centrality)

[1] Füller, J., Hutter, K., Hautz, J., & Matzler, K. (2014). User Roles and Contributions in Innovation-Contest Communities. Journal of Management Information Systems, 31(1), 273–308. https://doi.org/10.2753/MIS0742-1222310111

### Average number of replies to initial contribution

- [``avg number of replies``](../reference/pici/metrics/basic/#pici.metrics.basic.replies_to_initial_post)

[1] Yuan, X., Yang, S., & Wang, C. (2017). Lead user identification in online user innovation communities: A method based on random forest classification. *2017 7th IEEE International Conference on Electronics Information and Emergency Communication (ICEIEC), 157–160.* https://doi.org/10.1109/ICEIEC.2017.8076534


## Expertise

### PageRank

[1] Zhang, J., Ackerman, M. S., & Adamic, L. (2007). Expertise Networks in Online Communities: Structure and Algorithms. *WWW ’07: Proceedings of the 16th International Conference on World Wide Web, 221–230.*

[2] Agichtein, E., Castillo, C., & Donato, D. (2008). Finding High-Quality Content in Social Media. *Proceedings of the 2008 International Conference on Web Search and Data Mining, 11.*

### HITS

## Experience

### Topic re-occurence
<span class="label initial-contribution">initial contribution</span>

"The number of times a topic of the uploaded idea appeared in previous own ideas".

[1] Resch, C., & Kock, A. (2020). The influence of information depth and information breadth on brokers’ idea newness in online maker communities. *Research Policy, 104142.* https://doi.org/10.1016/j.respol.2020.104142

### Previous knowledge domains
<span class="label initial-contribution">initial contribution</span>

"The number of different knowledge domains with which an individual engaged in previous own ideas"

[1] Resch, C., & Kock, A. (2020). The influence of information depth and information breadth on brokers’ idea newness in online maker communities. *Research Policy, 104142.* https://doi.org/10.1016/j.respol.2020.104142

### Tenure

<span class="label contributor">contributor</span>

TODO:would have to include data since forum inception..?!

- [``days since first contribution``](../reference/pici/metrics/basic/#pici.metrics.basic.days_since_first_contribution)

### Absolute contribution

<span class="label contributor">contributor</span>

Number of contributions, number of intial contributions.

- [``number of contributions``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``number of initial contributions``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_initial_contributions)

### Normalized contribution

<span class="label contributor">contributor</span>

Number of contributions, number of initial contributions; normalized by time spent in community / length of contribution / number of replies to initial contribution

- [``number of contributions``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``number of initial contributions``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_initial_contributions)

### Out-degree centrality

<span class="label contributor">contributor</span>

## Diversity of contributions

### Sub-forum diversity
<span class="label contributor">contributor</span>

The diversity of a contributor's contributions in regard to which sub-forum they were made to. Diversity is either defined as a) *total number of different sub-forums*, or b) *the entropy of contributing behavior in gerade to sub-forum "classes"*. Each metric is defined for both 1) *all contributions*, and 2) *inital contributions* only.

- [``number of sub-forums contributed to``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``number of sub-forums made inital contributions to``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``entropy of sub-forums contributed to``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``entropy of sub-forums made inital contributions to``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)

### Links to external resources

### Content distance

## Providing assistance

## Past success

## Network position

### Fuger-role

<span class="label contributor">contributor</span>

#### Concept

Contributors can be classified by how much they engage in discussions by commenting (reacting to initial contributions), versus how much they initially contribute themselves. [1] distinguish the four classes "collaborator", "contributor", "allrounder", and "passive user". For example, "collaborators" are contributors that are often involved in discussions, but do not often contribute own ideas. Their contributions were found to be of higher quality in a crowdsourcing context [1].

[1] constructed a social network of "actor-to-actor relationships" "based on comments written on ideas". They used in-degree (comments received) and out-degree (comments given), as well as the number of contributions (ideas, stories, etc.) to determine user clusters (k-means) and users' roles. Qualitatively, their classification/clustering results can be summarized as:

|              | In-degree | Out-degree | Contributions |
|--------------|-----------|------------|---------------|
| Collaborator | High      | High       | Low           |
| Contributor  | High      | High       | High          |
| Allrounder   | Medium    | Medium     | Medium        |
| Passive user | Low       | Low        | Low           |

#### Metrics

This group of metrics assigns one of the four classes to each contributor: It uses the co-contribution network to determine each user's number of "received" and "given" comments (weighted in- and out-degree). In- and out-degree and number of initial posts form the basis for a community-level clustering with a fixed number of four clusters. Cluster centers are then ranked, and cluster labels assigned according to the table above. 

*Implemented:*

Contributor:
- [``fuger-role``](../reference/pici/metrics/basic/#pici.metrics.network.fuger_role)

Topic:
- [``first post by collaborator``](../reference/pici/metrics/basic/#pici.metrics.network.first_post_fuger_role)
- [``first post by contributor``](../reference/pici/metrics/basic/#pici.metrics.network.first_post_fuger_role)
- [``first post by allrounder``](../reference/pici/metrics/basic/#pici.metrics.network.first_post_fuger_role)
- [``first post by passive user``](../reference/pici/metrics/basic/#pici.metrics.network.first_post_fuger_role)

[1] Fuger, S., Schimpf, R., Füller, J., & Hutter, K. (2017). User roles and team structures in a crowdsourcing community for international development - a social  network perspective. *Information Technology for Development, 23(3)*, 438-462. https://doi.org/10.1080/02681102.2017.1353947

### Fueller-role

<span class="label contributor">contributor</span>

#### Concept

In the context of innovation-contest communities, [1] define six contributor roles by qualitative evaluation of contributor clusters, formed based on contribution patterns. Contribution patterns are defined on a co-contribution network using in-degree (comments directed towards contributor), out-degree (comments made by contributor), and number of contributions by contributor. The roles are labelled *socializer*, *idea generator*, *master*, *efficient contributor*, *passive idea generator*, and *passive commentator* (see table below). They find that  

|                        | In-degree | Out-degree | Contributions |
|------------------------|-----------|------------|---------------|
| Socializer             | Low       | High       | Low           |
| Idea generator         | Medium    | Low        | High          |
| Master                 | Very high | High       | Very high     |
| Efficient contributor  | Medium    | Low        | Medium        |
| Passive idea generator | None      | None       | Very low      |
| Passive commentator    | None      | Very low   | None          |

*Implemented:*

Contributor:
- [``fueller-role``](../reference/pici/metrics/basic/#pici.metrics.network.fueller_role)

Topic:
- [``first post by socializer``](../reference/pici/metrics/network/#pici.metrics.network.first_post_fuger_role)
- [``first post by idea generator``](../reference/pici/metrics/network/#pici.metrics.network.first_post_fuger_role)
- [``first post by master``](../reference/pici/metrics/network/#pici.metrics.network.first_post_fuger_role)
- [``first post by efficient contributor``](../reference/pici/metrics/network/#pici.metrics.network.first_post_fuger_role)
- [``first post by passive idea generator``](../reference/pici/metrics/network/#pici.metrics.network.first_post_fuger_role)
- [``first post by passive commentator``](../reference/pici/metrics/network/#pici.metrics.network.first_post_fuger_role)

[1] Füller, J., Hutter, K., Hautz, J., & Matzler, K. (2014). User Roles and Contributions in Innovation-Contest Communities. *Journal of Management Information Systems, 31(1),* 273–308. https://doi.org/10.2753/MIS0742-1222310111

### Lead user

<span class="label contributor">contributor</span>

### Hero

<span class="label contributor">contributor</span>

## Demographics

## Idea popularity

## Diversity of collaborators

## Sentiment
 
 <span class="label contribution">contribution</span> <span class="label initial-contribution">initial contribution</span> <span class="label thread">thread</span> 
 TO DO: <span class="label feedback">feedback</span>

### Concept

<p align="center">
    <img src="../images/Sentiment Table 1.jpg" width="700px" style="width: 55%; max-width:700px; min-width:300px;" />
</p>

[1] Anderson, N. H. (1971). Integration theory and attitude change. Psychological review, 78(3), 171. 
[2] Choi, J. N., Sung, S. Y., Lee, K., & Cho, D. S. (2011). Balancing cognition and emotion: Innovation implementation as a function of cognitive appraisal and emotional reactions toward innovation. Journal of Organizational Behavior, 32(1), 107-124.
[3] Kelman, H. C. (1958). Compliance, identification, and internalization three processes of attitude change. Journal of conflict resolution, 2(1), 51-60.
[4] Weiss, H. M., & Cropanzano, R. (1996). Affective events theory. Research in organizational behavior, 18(1), 1-74. 

### Subjective Sentiment

#### Polarity of words (Textblob, Sentiwordnet)

- [``avg_textblob_pol``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``aggregated_textblob_pol``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``avg_SWN_Polarity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``aggregated_SWN_Polarity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``idea_textblob_pol``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``idea_SWN_Polarity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``avg_feedback_textblob_pol``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``aggregated_feedback_textblob_pol``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``aggregated_feedback_SWN_Polarity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO

#### Subjectivity of words (Textblob, Sentiwordnet)

- [``avg_textblob_sub``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``aggregated_textblob_sub``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``avg_SWN_Subjectivity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``aggregated_SWN_Subjectivity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``idea_textblob_sub``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``avg_feedback_SWN_Subjectivity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``avg_feedback_textblob_sub``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``aggregated_feedback_textblob_sub``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``aggregated_feedback_SWN_Subjectivity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO

### Positive Sentiment

#### Proportion of positive words

- [``idea_pos_prop``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``avg_feedback_pos_prop``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``aggregated_feedback_pos_prop``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``avg_pos_prop``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``aggregated_pos_prop``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO

#### Mean positivity of words

- [``idea_mean_positivity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``avg_feedback_mean_positivity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``aggregated_feedback_mean_positivity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``avg_mean_positivity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``aggregated_mean_positivity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO

### Negative Sentiment

#### Proportion of negative words
- [``idea_neg_prop``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``avg_feedback_neg_prop``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``aggregated_feedback_neg_prop``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``avg_neg_prop``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``aggregated_neg_prop``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Mean negativity of words

- [``idea_mean_negativity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``avg_feedback_mean_negativity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``aggregated_feedback_mean_negativity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``avg_mean_negativity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``aggregated_mean_negativity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

### Diverse Sentiment

#### Standard Deviation of Polarity of words (Textblob, Sentiwordnet)

- [``std_textblob_pol``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``std_SWN_Polarity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Standard Deviation of Subjectivity of words (Textblob, Sentiwordnet)

- [``std_textblob_sub``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions)
- [``std_SWN_Subjectivity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Standard Deviation of Mean positivity of words

- [``std_mean_positivity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Standard Deviation of Mean negativity of words

- [``std_mean_negativity``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

[1] Beretta, M. (2019). Idea selection in web‐enabled ideation systems. Journal of Product Innova-tion Management, 36(1), 5-23.
[2] Chan, K. W., Li, S. Y., Ni, J., & Zhu, J. J. (2021). What feedback matters? The role of experience in motivating crowdsourcing innovation. Production and Operations Management, 30(1), 103-126.
[3] Lee, H., Choi, K., Yoo, D., Suh, Y., Lee, S., & He, G. (2018). Recommending valuable ideas in an open innovation community: a text mining approach to information overload prob-lem. Industrial Management & Data Systems.
[4] Lee, H., & Suh, Y. (2016). Who creates value in a user innovation community? A case study of MyStarbucksIdea. com. Online Information Review.
[5] Piezunka, H., & Dahlander, L. (2015). Distant search, narrow attention: How crowding alters or-ganizations’ filtering of suggestions in crowdsourcing. Academy of Management Journal, 58(3), 856-880.

## Openness

## Elaboration

 <span class="label contribution">contribution</span> <span class="label thread">thread</span> 

### Concept

Elaboration is associated with the degree of quality, readability, and complexity of the semantic depiction of contributions, and is characterized by two main aspects: text quantity and linguistic style. Based on the Geneplore Model, novel creations are the product of preinventive idea generation and exploration. If preinventive ideas are characterized by originality (distinctiveness) and appropriateness (elaboration, relevance), the exploration of novel and desired attributes can lead to creative output. Furthermore, based on Elaboration Theory, there are certain linguistic indicators that influence writing quality and content comprehension. Writing quality is characterized by lexical sophistication and syntactic complexity and contains fewer errors. Additionally, studies have shown that more successful writers produce longer texts. A more pronounced elaboration indicates that the author is a more knowledgeable and trustworthy expert on the topic. Accordingly, the best-elaborated contributions with a relevant amount of information, and a concise and readable presentation, are more likely to be evaluated, implemented, and reproduced. 

<p align="center">
    <img src="../images/Elaboration Table 1.jpg" width="700px" style="width: 55%; max-width:700px; min-width:300px;" />
</p>

[1] Crossley, S. A., Kyle, K., & McNamara, D. S. (2016). The development and use of cohesive de-vices in L2 writing and their relations to judgments of essay quality. Journal of Second Language Writing, 32, 1-16.
[2] Crossley, S. A., Roscoe, R., & McNamara, D. S. (2011, June). Predicting human scores of essay quality using computational indices of linguistic and textual features. In International conference on artificial intelligence in education (pp. 438-440). Springer, Berlin, Heidelberg.
[3] Finke, R. A., Ward, T. B., & Smith, S. M. (1996). Creative cognition: Theory, research, and ap-plications. MIT press.
[4] Finke, R. A., & Slayton, K. (1988). Explorations of creative visual synthesis in mental image-ry. Memory & cognition, 16(3), 252-257.

### High Elaboration

#### Length of text (number of words)
- [``avg_thread_length``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 
- [``aggregated_thread_length``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Number of syllables
- [``avg_number_syllables_thread``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 
- [``aggregated_number_syllables_thread``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Punctuation Density (Proportion of all characters)
- [``avg_content_punctuation_prop_thread``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 
- [``aggregated_content_punctuation_prop_thread``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Spacing Density (proportion of all characters)
 
#### Capitalization Density (proportion of all characters)
 
#### Flesch-Reading-Ease Score
- [``flesch_reading_ease``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Automatic Readability Index
- [``automated_readability_index``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

### Complex Elaboration

#### Number of References (links)
- [``avg_neg_prop``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 
- [``aggregated_neg_prop``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Flesch-Kincaid Formula
- [``flesch_kincaid_grade``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Smog Grading
- [``smog_index``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Coleman-Lieau Index
- [``coleman_liau_index``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Dale-Chall Readbility Score
- [``dale_chall_readability_score``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Number of difficult words
- [``difficult_words``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

#### Linsear Write Formula
- [``linsear_write_formula``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

### Low Elaboration

#### Number of Spelling Mistakes
- [``avg_spelling_mistakes_thread``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``aggregated_spelling_mistakes_thread``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO  
 
#### Number of Punctuation Mistakes
- [``avg_content_punctuations_thread``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 
- [``aggregated_content_punctuations_thread``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO 

[1] Agichtein, E., Castillo, C., Donato, D., Gionis, A., & Mishne, G. (2008, February). Finding high-quality content in social media. In Proceedings of the 2008 international conference on web search and data mining (pp. 183-194).
[2] Beretta, M. (2019). Idea selection in web‐enabled ideation systems. Journal of Product Innova-tion Management, 36(1), 5-23.
[3] Di Gangi, P. M., & Wasko, M. (2009). The co-creation of value: Exploring user engagement in user-generated content websites. In Proceedings of JAIS theory development workshop. sprouts: working papers on information systems (Vol. 9, No. 50, pp. 9-50).
[4] Grosse, M., Pohlisch, J., & Korbel, J. J. (2018). Triggers of collaborative innovation in online user communities. Journal of Open Innovation: Technology, Market, and Complexity, 4(4), 59.
[5] Lee, H., Choi, K., Yoo, D., Suh, Y., Lee, S., & He, G. (2018). Recommending valuable ideas in an open innovation community: a text mining approach to information overload prob-lem. Industrial Management & Data Systems.
[6] Lee, H., & Suh, Y. (2016). Who creates value in a user innovation community? A case study of MyStarbucksIdea. com. Online Information Review.
[7] Li, M., Kankanhalli, A., & Kim, S. H. (2016). Which ideas are more likely to be implemented in online user innovation communities? An empirical analysis. Decision Support Systems, 84, 28-40.
[8] Nagar, Y., De Boer, P., & Garcia, A. C. B. (2016). Accelerating the review of complex intellectual artifacts in crowdsourced innovation challenges.
[9] Piezunka, H., & Dahlander, L. (2015). Distant search, narrow attention: How crowding alters or-ganizations’ filtering of suggestions in crowdsourcing. Academy of Management Journal, 58(3), 856-880.
[10] Resch, K., Fellner, M., Fahrenwald, C., Slepcevic-Zach, P., Knapp, M., & Rameder, P. (2020). Embedding Social Innovation and Service Learning in Higher Education's Third Sector Policy Developments in Austria. In Frontiers in Education (p. 112). Frontiers.
[11] Rhyn, M., & Blohm, I. (2017). A machine learning approach for classifying textual data in crowdsourcing.

## Distinctiveness

 <span class="label contribution">contribution</span> <span class="label thread">thread</span> 

### concept

This PI factor refers to the uniqueness and novelty of a contribution by capturing the degree of similarity of the current contribution to previous ones in the PI community. Distinct contributions discuss concepts that are substantially different from prior ideas, contain distant knowledge and novelty. Based on Creative Cognition Theory, if preinventive ideas are characterized by originality (distinctiveness) and appropriateness (elaboration, relevance), the exploration of novel and desired attributes can lead to creative output. Characterizing a problem more abstractly rather than considering specific solutions to previous problems is less constraining and more likely to lead to innovation. The concept of Distant Knowledge, based on the Attention-based View and research on Information Overload, highlights that novelty and abstraction in problem formulation can foster creativity in subsequent processing. Promising ideas have an optimal level of creativity, balance novelty with familiarity, and are associated with rarity and high user demand.

<p align="center">
    <img src="../images/Distinctiveness Table 1.jpg" width="700px" style="width: 55%; max-width:700px; min-width:300px;" />
</p>

[1] Hoornaert, S., Ballings, M., Malthouse, E. C., & Van den Poel, D. (2017). Identifying new product ideas: waiting for the wisdom of the crowd or screening ideas in real time. Journal of Product Innovation Management, 34(5), 580-597.
[2] Huber, G. P., & Daft, R. L. (1987). The information environments of organizations.
[3] Ocasio, W. (1997). Towards an attention‐based view of the firm. Strategic management journal, 18(S1), 187-206.
[4] Piezunka, H., & Dahlander, L. (2015). Distant search, narrow attention: How crowding alters or-ganizations’ filtering of suggestions in crowdsourcing. Academy of Management Journal, 58(3), 856-880.
[5] Thorleuchter, D., Van den Poel, D., & Prinzie, A. (2010). Mining ideas from textual infor-mation. Expert Systems with Applications, 37(10), 7182-7188.
[6] Toubia, O., & Netzer, O. (2017). Idea generation, creativity, and prototypicality. Marketing sci-ence, 36(1), 1-20.

### High Distinctiveness

#### TF.IDF-indices (Specificity) 

- [``tfidf_sum``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO
- [``tfidf_avg``](../reference/pici/metrics/basic/#pici.metrics.basic.number_of_contributions) # TO DO  

#### Topic Structure with LDA
probability per topic (total number of topics depends on highest coherence score)

[1] Resch, K., Fellner, M., Fahrenwald, C., Slepcevic-Zach, P., Knapp, M., & Rameder, P. (2020). Embedding Social Innovation and Service Learning in Higher Education's Third Sector Policy Developments in Austria. In Frontiers in Education (p. 112). Frontiers.
[2] Rhyn, M., & Blohm, I. (2017). A machine learning approach for classifying textual data in crowdsourcing.

## Community feedback

## Activity level

## Prominence

## Crowd vs community

### Lorenz curve

<span class="label community">community</span>

#### Concept

The Lorenz curve of % posts (x-axis) made by % contributors (y-axis) can be used to indicate contribution inequality in communities.

#### Metrics

Community:
- [``% contributors`` + ``% posts``](../reference/pici/metrics/basic/#pici.metrics.basic.lorenz)

#### Visualizations

- [``plot_lorenz_curves``](../reference/pici/visualizations/#pici.visualizations.plot_lorenz_curves)
