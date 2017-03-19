# Log-Parser
**A modular log parser that parses apache logs and stores processed logs as CSV.**

This code generatea host sessions from raw log and assign session id to every line in the log. <br />
Definition of session: Session is window of activity from a host. A session ends when there is at least 15 mins of inactivity.
 
**Input raw log schema:**<br />
\<host name> \<log name> \<time> \<method> \<url> \<response> \<bytes> <br />
Sample: piweba3y.prodigy.com - 807301196 GET /shuttle/missions/missions.html 200 8677<br />
 
**Processed log / session schema:**<br />
\<host name>,\<session ID>,\<date DD-MM-YYYY>,\<time HH:MM:SS>,\<method>,\<response> <br />
Sample: piweba3y.prodigy.com, piweba3y.prodigy.com_1, 01-08-1995, 18:19:56, GET, 200<br />

### Dataset: <br />
NASA Apache Web Logs (http://opensource.indeedeng.io/imhotep/docs/sample-data/):<br />
nasa_19950630.22-19950728.12.tsv.gz<br />
nasa_19950731.22-19950831.22.tsv.gz
