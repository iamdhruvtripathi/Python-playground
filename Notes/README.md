### `mini_siem.py`

* Reads real Windows Security Event Logs directly
* Uses the Windows Event Log API through `pywin32`
* Does not require copying logs or using fake data
* Parses event information such as Event ID, time, username, and IP when available
* Applies simple detection rules to the events
* Detects things like repeated failed logins or suspicious activity
* Generates alerts and displays them in the terminal
* Can later save alerts, add severity levels, filtering, and a dashboard

**Architecture:**

```text
Windows Security Event Log
            ↓
         pywin32
            ↓
       mini_siem.py
            ↓
      Parse events
            ↓
     Detection rules
            ↓
          Alerts
```
