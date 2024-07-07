import React from "react"

const PlayerList = ({players}) => {
    return <div>
        <h2>Players</h2>
        <table>
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Email</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {players.map((player) => (
                    <tr key={player.id}>
                        <td>{player.firstName}</td>  
                        <td>{player.lastName}</td> 
                        <td>{player.email}</td>   
                        <td>
                            <button>Update</button>
                            <button>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>

    </div>


}

export default PlayerList