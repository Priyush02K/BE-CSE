Experiment No. 1

Aim:
    Perform Email Header Analysis for extracting valuable information like sender IP address, email servers, and routing information.
  . Conduct email address enumeration by attempting to verify the existence of email addresses within a target domain. Use tools like the Harvester or thehunter.io to search for email addresses associated with a specific domain. This can help identify valid email addresses within an organization.
  . Analyze the metadata of an email, including date and time stamps, email clients used, or the originatingIP address, email's origin, potential geographic location of the sender, or possible email routing

Part 1: Email Header Analysis
Step 1: Obtain an Email Header
    Gmail
    Open Gmail.
    Open any email you own or have permission to inspect.
    Click the three dots (⋮) near the Reply button.
    Select Show Original.
    Copy the complete email header.

Step 2: Analyze Header Manually
| Field       | Purpose               |
| ----------- | --------------------- |
| From        | Sender email          |
| To          | Receiver              |
| Date        | Time sent             |
| Message-ID  | Unique email ID       |
| Return-Path | Actual sender         |
| Received    | Email route           |
| SPF         | Sender authentication |
| DKIM        | Email signature       |
| DMARC       | Anti-spoofing policy  |



Step : Use Online Header Analyzer

Paste the copied header into an email header analyzer such as MXToolbox's analyzer.
https://mxtoolbox.com/SuperTool.aspx 
The analyzer provides:

Sender IP
Mail servers
SPF status
DKIM status
DMARC result
Delivery path

Part 2: Email Address Enumeration

Step 1

  Visit Hunter.io.

Step 2

  Enter a domain.

Example

  example.com
Step 3

  Click Search.

Results may include:

  john@example.com
  
  admin@example.com
  
  sales@example.com
  
  support@example.com

Method 2: theHarvester (Kali Linux)
Step 1

  Open Terminal

Step 2

Run

  theHarvester -d example.com -b all

Where

  -d

domain

  -b

search engine

Step 3

Wait for scanning.

Output example

Emails Found

admin@example.com

info@example.com

support@example.com

It may also discover:

Hosts
Subdomains
Public IPs

depending on the selected data sources.


Part 3: Email Metadata Analysis
Step 1

Open the email header.

Step 2

Locate the Date

Example

Date:

  Tue, 10 Jun 2025
  
  11:25:30 +0530

  This indicates the send time and time zone.

Step 3

Find Message-ID

Example

  Message-ID:
  <abc123@mail.example.com>

This uniquely identifies the message.


Step 4
  
  Find Email Client
  
  Look for headers like
  
  User-Agent:
  
  or
  
  X-Mailer:
  
  Example
  
  X-Mailer:
  
  Microsoft Outlook 365
  
  or
  
  User-Agent:
  
  Mozilla Thunderbird


Step 5

Identify Mail Servers

Example

  Received:
  
  from smtp.example.com
  
  by gmail.com
  
  Shows the sending and receiving mail servers.

Step 6
  Determine Geographic Location (if a public IP is available)
  
  Extract the public IP address from the header and use an IP geolocation service to estimate:
  
  Country
  City (approximate)
  ISP
  Organization
  
  Keep in mind that this identifies the IP owner's location (often a mail server or VPN), not necessarily the sender's physical location.
