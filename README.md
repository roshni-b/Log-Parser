# Log-Parser
**A modular log parser that parses NASA's Apache Web logs and stores processed logs as CSV.**

This code generates host sessions from raw log and assign session id to every line in the log. <br />
Definition of session: Session is window of activity from a host. A session ends when there is at least 15 mins of inactivity.
 
**Input (Raw) log schema:**<br />
\<host name>  \<log name>  \<time>  \<method>  \<url>  \<response>  \<bytes> <br />
Sample: `piweba3y.prodigy.com - 807301196 GET /shuttle/missions/missions.html 200 8677`<br />
 
**Output (Processed) log schema:**<br />
\<host name>, \<session ID>, \<date DD-MM-YYYY>, \<time HH:MM:SS>, \<method>, \<response> <br />
Sample: `piweba3y.prodigy.com, piweba3y.prodigy.com_1, 01-08-1995, 18:19:56, GET, 200`<br />

| Field name | Description                                                                                        |
|----------|------------------------------------------------------------------------------------------------------|
| host     | When possible, the hostname making the request. Uses the IP address if the hostname was unavailable. |
| logname  | Unused, always -                                                                                     |
| time     | In seconds, since 1970                                                                               |
| method   | HTTP method: GET, HEAD, or POST                                                                      |
| url      | Requested path                                                                                       |
| response | HTTP response code                                                                                   |
| bytes    | Number of bytes in the reply                                                                         |

### Dataset: <br />
NASA Apache Web Logs (http://opensource.indeedeng.io/imhotep/docs/sample-data/):<br />
- [nasa_19950630.22-19950728.12.tsv.gz](http://indeedeng.github.io/imhotep/files/nasa_19950630.22-19950728.12.tsv.gz)
- [nasa_19950731.22-19950831.22.tsv.gz](http://indeedeng.github.io/imhotep/files/nasa_19950731.22-19950831.22.tsv.gz)

**Pre-processing**<br />
Some of the host names have commas - these have been replaced by dots. This ensures that while reading the .csv file, the part of the host name that comes after the comma does not get read as log name instead (which is the next column), consequently all the other attributes in the same log entry are prevented from bring misread. <br />

## Usage: <br />

##### 1. Cloning the repository.
```
git clone https://github.com/roshni-b/Log-Parser.git
cd Log-Parser
```
##### 2. Decompressing log files.
```
gunzip nasa_19950630.22-19950728.12.tsv.gz
gunzip nasa_19950731.22-19950831.22.tsv.gz
```
##### 3. Running the [script](https://github.com/roshni-b/Log-Parser/blob/master/LogParser.py).
```
python LogParser.py
```
