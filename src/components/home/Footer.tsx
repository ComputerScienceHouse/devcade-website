import React from "react";
import '../../index.tsx.css';
import '../../css/footer.css';

const Footer: React.FunctionComponent = () => {

    return (
        <div id="footer">
            <div id="footer-quote">
                <p>"For developers, by developers"</p>
            </div>

            <div id="footer-links" className="footer-flex">
                <a href="https://csh.rit.edu">
                    <div className="link">
                        <img alt="CSH" src="./icons/csh_logo_square.svg" />
                    </div>
                </a>

                <a href="https://github.com/ComputerScienceHouse/?q=devcade">
                    <div className="link">
                        <img alt="GitHub" src="./icons/github.svg" />
                    </div>
                </a>

                <a href="https://instagram.com/ComputerScienceHouse">
                    <div className="link">
                        <img alt="Instagram" src="./icons/instagram.svg" />
                    </div>
                </a>

                <a href="https://twitter.com/RITCSH">
                    <div className="link">
                        <img alt="Twitter" src="./icons/twitter.svg" />
                    </div>
                </a>
            </div>
        </div>
    )
}

export default Footer