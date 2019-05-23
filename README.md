# Friend Fund
Custodian-less Investment using Payment Channels and Rainbow Transactions on the Litecoin Lightning Network.

## Project Description
Friend Fund is a software package the empowers investment funds to use Litecoin and the Lightning network to send and receive investment, dividends, and management fees securely without any custodians or other third party involvement.

## Technical Description
Friend Fund is deployable to Kubernetes and uses Docker images for Litecoin and Lightning. The application is a Python Flask project with a minimalist user interface. The client and server are a single application. Friend Fund generally supports:
* Opening Litecoin payment channels
* Issuing invoices against payment channels
* Approving invoices against payment channels
* Closing Litecoin payment channels

## Business Description
Friends Fund works on the idea of that a lightning transaction can be opened, LTC can be committed, and LTC can be transferred in small amounts. A fund can take a fee and offer exposure to some risk, where accounts can be managed using a _continuously cash settled_ method on top of the lightning network.
