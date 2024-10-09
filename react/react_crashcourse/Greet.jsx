const Greet = ({ userName }) => {
  const numbers = [27, 31];
  const cast = [
    { name: 'Natalie Portman', BirthPlace: 'Jerusalem' },
    { name: 'Blake Lively', BirthPlace: 'LA' },
  ];

  let now = new Date().getHours();
  let greeting;
  if (now < 12) {
    greeting = 'Good Morning';
  } else if (now < 18) {
    greeting = 'Good Afternoon';
  } else {
    greeting = 'Good Evening';
  }

  const Button = () => {
    return <button onClick={() => console.log('sup?')}>Click</button>;
  };

  return (
    <div>
      <h2>
        {greeting} **{userName}**
      </h2>
      <p>Did you know that 1 + 2 = {1 + 2}?</p>
      <ul>
        <li>Zzz</li>
        {numbers.map(n => (
          <li key={n}>{n}</li>
        ))}
      </ul>

      <ul>
        <h2>Welcome the cast:</h2>
        {cast.map(({ name, BirthPlace }, idx) => (
          <li key={idx}>
            {name} - Born in {BirthPlace}
          </li>
        ))}
      </ul>

      <Button />
    </div>
  );
};

export default Greet;
