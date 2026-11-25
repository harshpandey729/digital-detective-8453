# Mission 7 - How computers communicate

## 1. Task / objective
Explain LAN, MAN, WAN, DNS, routers, protocols, packet switching and client-server communication.

## 2. Work completed
Documented network concepts and the steps used to open a website.

## 3. Commands / tools used
- `curl -I --max-time 10 https://example.com`: connectivity and HTTP response check.
- Python `socket.getaddrinfo("example.com", 443, type=socket.SOCK_STREAM)`: resolve a public domain to network addresses.

### Network concepts

| Concept | Explanation | Example |
|---|---|---|
| LAN | A network covering a small location | Home or lab |
| MAN | A network covering a city or large campus | University campus network |
| WAN | A network spanning broad geographical areas | The internet |
| DNS | Resolves a domain name into network addresses | `example.com` lookup |
| Router | Forwards network traffic between networks | Home or campus router |
| Protocol | A shared set of communication rules | HTTP/HTTPS or TCP/IP |
| Packet switching | Splits data into packets that can be forwarded independently | Web page data divided into packets |
| Client-server | A client requests a service and a server responds | Browser requesting a website |

### Connectivity observations

The HTTPS connectivity check returned `HTTP/2 200` from `example.com`, showing that the host responded to the request. The DNS lookup returned the public IPv4 addresses `172.66.147.243` and `104.20.23.154`. A connectivity test checks whether a host can be reached and respond; a DNS lookup shows address information associated with a domain. DNS lets a browser use a human-readable name rather than requiring a person to enter a network address.

### Website communication

1. The browser acts as a client and receives the website address.
2. The browser sends the domain to DNS to resolve an address.
3. DNS returns the matching network address information.
4. The browser uses the router and internet to send a request.
5. Network protocols divide and carry the request as packets.
6. The server receives it and returns a response containing page resources.
7. The browser interprets the response and displays the website.

## 4. My understanding
Networks connect devices, DNS translates names, routers forward traffic, protocols define communication rules and packet switching allows data to travel efficiently.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Used public example domains and recorded no private network details.

## 7. Evidence / files
Network concept table and privacy-safe website steps in this README.

## 8. Commit details
Commit message: `Explain networking concepts and website communication`
