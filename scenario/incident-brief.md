# Incident Brief: IR-001

## Case Title
Suspected Brute-Force Login Followed by Successful Authentication

## Organisation
Northstar Retail Ltd. (fictional)

## Incident ID
IR-001

## Date
15 October 2026

## Initial Alert
The monitoring team observed repeated failed authentication attempts against the account `j.smith`, followed by a successful login from the same source IP address.

## Systems Involved
- Host: `WS-014` (fictional workstation)
- Account: `j.smith` (fictional employee account)
- Log source: Synthetic authentication event records

## Investigation Objectives
1. Establish the sequence of authentication events.
2. Determine whether the activity meets the detection criteria for a suspected brute-force attempt.
3. Establish whether the successful login is suspicious and whether compromise is confirmed.
4. Assess the potential impact and severity.
5. Recommend containment, remediation and validation steps.
6. Produce a final incident report supported by evidence.

## Scope and Limitations
This investigation uses synthetic log data created for educational purposes. It does not represent activity observed on a real company's network. No real account, IP reputation or system compromise is implied.

## Initial Hypothesis
Repeated failed logins followed by a successful login may indicate a brute-force attempt. Alternative explanations, including a user repeatedly entering an incorrect password, must also be considered.

## Expected Deliverables
- Initial triage notes
- Authentication event timeline
- Evidence and findings
- Incident classification and severity rationale
- Containment and remediation recommendations
- Final incident report
- Lessons learned