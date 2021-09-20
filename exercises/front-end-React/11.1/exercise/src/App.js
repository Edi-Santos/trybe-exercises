import './App.css';

const Task = (value) => {
  return (
    <li>{value}</li>
  );
}

const TaskList = ['Estudar pela manhã.', 'Estudar pela tarde.', 'Estudar pela noite.'];

const WalksTaskList = TaskList.map((task) => `${task} `);

function App() {
  return (
    <main>
      {Task('só de bob')}
      {WalksTaskList}
    </main>
  );
}

export default App;
