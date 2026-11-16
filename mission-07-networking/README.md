# Mission 7 - How computers communicate

## 1. Task / objective
Explain networks, check connectivity and DNS, and describe how a browser opens a website.

## 2. Work completed
### 7.1 Network concepts

| Concept | Meaning | Example |
| --- | --- | --- |
| LAN | A network in a small area | Computers on a home or lab network |
| MAN | A network spanning a metropolitan area | Links between offices across one city |
| WAN | A network spanning large distances | A company's network between different countries |
| DNS | Looks up records associated with a domain name, including IP addresses | Finding an address for `example.com` |
| Router | Forwards packets between networks | A home router forwarding traffic towards the ISP |
| Protocol | Agreed rules for communication | HTTP for web requests and responses |
| Packet switching | Split data into packets that are forwarded through a network | A file transfer travelling in many packets |
| Client-server | A client requests a service from a server | A browser requesting a page from a web server |

The internet connects many networks. A home LAN usually reaches it through a router and an internet provider.

### 7.2 Actual network observations

| Command | Observation | What it checks |
| --- | --- | --- |
| `ping -c 3 -W 1000 example.com` | 3 sent, 3 received; 0% loss; average 46.616 ms | Whether the remote host replies to ICMP echo requests and approximate round-trip time |
| `nslookup example.com 1.1.1.1` | Two address answers were returned | A DNS lookup through a public resolver |
| `curl -I --max-time 15 https://example.com` | `HTTP/2 200`; HTML content type | Whether an HTTPS request can reach the website |

IP addresses have been removed from the saved results. `1.1.1.1` in the command is the chosen public resolver, not the computer's private DNS or IP address.

A successful ping does not prove that a website works; it checks a different protocol. A failed ping also does not prove the site is down, because networks may block ICMP. The HTTPS check gives separate evidence about the web service.

A DNS lookup shows the queried name and returned records, such as address records. Here the answer was labelled non-authoritative because it came from a recursive resolver rather than directly from the domain's authoritative server. DNS helps the browser obtain an address without making the user memorise it.

### 7.3 Opening an HTTPS website

1. The browser acts as the **client**. It reads the website name and may first check its caches.
2. If an address is not cached, **DNS** is used to find an address for the domain.
3. Packets travel through the local network, a **router**, the ISP and other networks towards the destination.
4. The client establishes a connection and negotiates encryption for HTTPS. HTTP/1.1 and HTTP/2 normally use TCP with TLS; HTTP/3 uses QUIC.
5. The browser sends an HTTP request. The **server** handles it and sends a response containing a status, headers and usually page data.
6. The browser reads the HTML, requests other resources such as CSS and images, and displays the page. HTTP and the transport **protocols** define how those exchanges work.

## 3. Commands / tools used
`ping` for a bounded connectivity test, `nslookup` for DNS and `curl -I` for HTTP response headers. The commands targeted the public example domain, not a private device.

## 4. My understanding
DNS finds an address, routers forward packets, and the server provides the requested content. These are separate parts of opening a website. Network timings and DNS answers can change between runs.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
[Redacted network checks](../evidence/mission-07-network.txt).

## 8. Commit details
Commit message: `Explain networking concepts and website communication`.

Published in this repository's [commit history](https://github.com/Mayanksuthar07/digital-detective-8508/commits/main/).
