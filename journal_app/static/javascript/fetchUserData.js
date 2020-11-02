
'use strict';

let numberOfUsers = document.getElementById('total-number-of-users')

/**
 * Function: getUserData
 * 
 * @description Retrieve user data from database
 *  
 * 
 * 
 * @return Users    - Containing @total_users, @valid
 *                          
 *         
 * 
 */
let Users = {'data': 0};
export const getUsersData = (totalUserID=numberOfUsers) =>{
    
    fetch('http://127.0.0.1:8000/journal/dashboard/data', {
    method: 'GET', // or 'PUT'
    headers: {
        'Content-Type': 'application/json',
    },
    })
    .then(response => response.json())
    .then(data => {
        Users = {'data': data}
        totalUserID.innerHTML = Users.data.total_users;
    })
    .catch((error) => {
    console.error('Error:', error);
    });
    return Users;
}
