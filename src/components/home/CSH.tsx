import React from "react";
import '../../css/homegrid.css';
import '../../index.tsx.css';

const CSH: React.FunctionComponent = () => {

    return (
        <div className="cshbox">
            <h2 className="cshbox-header">What is CSH?</h2>

            <p className="cshbox-info">
                Since 1976, <a className="bodylink" href="https://csh.rit.edu">Computer Science House</a> (CSH) has
                provided a living-learning environment for its members. CSH is a Special Interest House at RIT with
                mulitple lounges, workrooms, study areas, and a datacenter, all on one dorm floor.
            </p>

            <p className="cshbox-info">
                Computer Science House provides its members with unique facilities, a strong social atmosphere,
                and has a strong emphasis on hands-on learning. CSH has a rich history of large-scale projects,
                including multiple internet-connected vending machine, providing &nbsp;
                <a className="bodylink" href="https://schedulemaker.csh.rit.edu">ScheduleMaker</a> to RIT students,
                and now Devcade.
            </p>
        </div>
    )
}

export default CSH