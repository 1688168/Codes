# Functional and non-functional requirements

## Functional Requirements (required system behavior)
> start from users and work backward
* Who the customers are
* How they use the system 
  
## Non-Functional Requirements (required quality of the system)
> High Availability
* Time-based and count-based availability
* Design principles behind high availability
* what does High-Availability mean?
  * A system that achieves 100% availability the past week doesn't mean it's high available.  (it is still the single point of failure)

* avoid single point of failure (build redundency)
* switch from one server to another without losing data.
* protect the system from atypical client behavior
* protect the system from failures and  performance degradation of its dependencies
* detect failures as they occur
* small downtime


> 'SLO'
* Service Level Objective (system goal)

> 'SLA'
* Service Level Agreement (with client)


> Fault tolerance == high availability ?
* Fault tolerance is the property that enables a system to continue operating properly in the event of one of more faults within some of its components.
* Error
* Fault
* Mistake
* High availability: downtime is possible and the system tries to minimize it.
* Fault tolerance: The System has the goal of zero downtime.
* A system is fault-tolerance is high available, but not the other way around
* airplane required fault tolerant: an engine is out, we still need to be able to fly safly until next step
* a car just need to be high available. when getting flat tire, we just experience a short down-time to replace it with spare tire.
* fault tolerance is with higher cost due to no down time requirements
* close to zero downtime

> Resilience
* Systems that in the face of faults can provide an maintain an acceptable level of service are called resilience system.
* ability to quickly recover from failure

> Reliability
* high availability + correctness + time
* system always performs it's intended functions correctly and in time

## User/Customers
## Scale (Read and Write)
## Performance
## Cost