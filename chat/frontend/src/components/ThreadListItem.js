import Avatar from './Avatar.js';
import './ThreadListItem.css';

function ThreadListItem() {
  // w-full
  const thread = {
    user: {
      avatar: 'https://avatars.githubusercontent.com/u/3273867?v=4',
      username: 'Emmanuel Lodovice',
    },
    message: 'This is a test message This is a test This is a test message This is a test ',
    timestamp: new Date()
  }
  const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  return (
    <div className="thread-list-item pr-3 py-2 hover:pl-3">
      <div className="flex items-center">
        <Avatar user={thread.user} />
        <div className="ml-4 text-content">
          <div className="flex items-center justify-between">
            <h4 className="text-lg">{thread.user.username}</h4>
            <span className="text-sm">{thread.timestamp.toLocaleDateString(options)}</span>
          </div>
          <p className="text-base text-slate-300 text-ellipsis overflow-hidden whitespace-nowrap">{thread.message}</p>
        </div>
      </div>
    </div>
  );
}

export default ThreadListItem;
