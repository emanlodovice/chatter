import { useContext } from 'react';
import Avatar from './Avatar.js';
import './ThreadListItem.css';
import { GlobalContext } from './../store';

function ThreadListItem(props) {
  const store = useContext(GlobalContext);
  const thread = props.thread;
  thread.user = thread.members.filter((member) => member.id !== store.state.userId)[0];
  thread.timestamp = new Date(thread.last_message_date);
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
          <p className="text-base text-slate-300 text-ellipsis overflow-hidden whitespace-nowrap">{thread.last_message}</p>
        </div>
      </div>
    </div>
  );
}

export default ThreadListItem;
