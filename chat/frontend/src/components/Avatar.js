import './Avatar.css';


function Avatar({user}) {
  return (
    <span className="avatar">
      <img src={user.avatar} alt={user.username} />
    </span>
  )
}

export default Avatar;