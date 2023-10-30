# Question 4: COVID Again?! [16 marks]

## Background [OK to skip] COVID-19 has been plaguing us since it was ﬁrst identiﬁed in Wuhan in December 2019. Today, as we continue to put in our best efforts to put an ‘end’ to the endemic, we shall instead see an ‘end’ to this midterms instead. 
Source: WikipediaAfter learning about Python in CS1010S, you are excited to know how to model existing contact-tracing efforts in Singapore.

Your ﬁrst task is to design a Record data type, which serves to model some key information concerning a place visit. The Record data type should be supported by the following functions:
- make_record(checkin, checkout, place) takes three strings: 
checkin and checkout are time-strings in "HHMM" 24-hour hour-minute format, and represent check-in and check-out timings to a place respectively. place represents a name-string of a place. 
It returns a data type representing a record.•get_checkin(record) takes in a record, and returns the check-in time-string

- get_checkout(record) takes in a record, and returns the check-out time-string.

- get_place(record) takes in a record, and returns the place name-string. 

Q4A. Decide on a data structure using tuples to represent a record, and implement the functions make_record,get_checkin,get_checkout, and get_place. [2 marks]


B. We are all familiar with TraceTogether, which helps keep track of an individual’s visits to multiple places. We say that a Trace data type is essentially a collection of Record objects aparticular person is linked to. The trace data type is supported by the following functions:

- make_trace(name, records_tpl) takes in a string representing a person’s name, and his or her visited tuple of Record objects. It returns a data type representing a trace.•get_person(trace) takes in a trace, and returns the person’s name.

- get_records(trace) takes in a trace, and returns the tuple containing one or moreRecord objects.

Q4B. Decide on a data structure using tuples to represent a trace, and implement the functions make_trace,get_person , and get_records [2 marks]



