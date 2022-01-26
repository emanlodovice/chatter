import Avatar from './Avatar.js';
import SearchForm from './SearchForm.js';
import ThreadListItem from './ThreadListItem.js';
import './ThreadList.css';

function ThreadList() {
  const user = {
    avatar: 'https://avatars.githubusercontent.com/u/3273867?v=4',
    username: 'emanlodovice'
  }
  return (
    <div className="thread-list">
      <div className="flex items-center">
        <Avatar user={user} />
        <h1 className="text-2xl font-bold ml-3">{user.username}</h1>
      </div>
      <SearchForm />
      <div className="items pt-2">
        <ThreadListItem />
        <ThreadListItem />
      </div>
    </div>
  );
}

export default ThreadList;
