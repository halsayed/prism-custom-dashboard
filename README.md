[![Contributors][contributors-shield]][contributors-url]
[![LastCommit][lastcommit-shield]][lastcommit-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#calminstallation">Automated Calm Installation</a></li>
        <li><a href="#manualinstallation">Manual Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://www.nutanix.com/products/prism)

This project aims at creating a fully customizable login HTML page for Nutanix Prism Central. In many cases, you would like to re-brand the first landing page when access Prism Central. This python-flask project simply displays an HTML form and passes the credentials to Prism Central to perform the actual authentication, upon successful authentication the user connection is proxied by Nginx to Prism Central directly. The flask application doesn't maintain any user credential or session data.


<!-- GETTING STARTED -->
## Getting Started

Follow the instructions below to deploy this custom login page in your environment.

### Prerequisites

To test this login page, the following is required:
- Nutanix Prism Central 5.16+
- For automated installation you will need Calm 3.1+
- For the manual installation you will need a machine with docker and docker-compose


### Calm Installation

1. Download and save the Calm blueprint to your local machine.
2. Upload the blueprint .json file to your Calm and launch.

### Manual Installation
1. Clone the repo to your local machine
```shell
git clone https://github.com/halsayed/prism-custom-dashboard.git
cd prism-custom-dashboard
```
2. Edit docker-compose.yaml replacing PRISM_HOST and PRISM_PORT with the correct values for your environment. Alternatively you can create .env file with these values.
3. run docker-compose
```shell
docker-compose up -d
```

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Husain Ebrahim - [@husainNTNX](https://twitter.com/husainNTNX)

Project Link: [https://github.com/halsayed/prism-custom-dashboard](https://github.com/halsayed/prism-custom-dashboard)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Login Form v1 by Colorlib](https://colorlib.com/wp/template/login-form-v1/)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/halsayed/prism-custom-dashboard?style=plastic
[contributors-url]: https://github.com/halsayed/prism-custom-dashboard/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/halsayed/prism-custom-dashboard?style=plastic
[forks-url]: https://github.com/halsayed/prism-custom-dashboard/network/members
[lastcommit-shield]: https://img.shields.io/github/last-commit/halsayed/prism-custom-dashboard?style=plastic
[lastcommit-url]: https://github.com/halsayed/prism-custom-dashboard/graphs/commit-activity
[stars-shield]: https://img.shields.io/github/stars/halsayed/prism-custom-dashboard?style=plastic
[stars-url]: https://github.com/halsayed/prism-custom-dashboard/stargazers
[issues-shield]: https://img.shields.io/github/issues/halsayed/prism-custom-dashboard?style=plastic
[issues-url]: https://github.com/halsayed/prism-custom-dashboard/issues
[license-shield]: https://img.shields.io/github/license/halsayed/prism-custom-dashboard?style=plastic
[license-url]: https://github.com/halsayed/prism-custom-dashboard/blob/master/LICENSE.txt
[product-screenshot]: images/prism-login.png
