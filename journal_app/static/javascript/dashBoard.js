
'use strict';
import { getUsersData } from './fetchUserData.js'

window.onload = function(){
    let totalUsersID = document.getElementById('total-number-of-users');
    let Users = {};
    
    
    getUsersData(totalUsersID);
    // console.log("dasbboard");
    // console.log(Users);
    // totalUsersID.innerHTML = Users.data.total_users;
    /**
     * myInterval       - Updating myFunc
     *                    per 3 sec using setInterval.        
     */
    let interval;
    const myInterval = () => {
        interval = setInterval(myFunc, 1000);
    }
    /**
     * myFunc           - received a call from setInterval
     *                    and update getUsersData per 3 sec.
     */
    const myFunc = () => {
         Users = getUsersData(totalUsersID);
    }
    myInterval();
   
}
