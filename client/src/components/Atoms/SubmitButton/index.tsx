import "./style.scss";
interface AppState {
  text: string;
}

export function SubmitButton({ text }: AppState) {
  var animateButton = function (e: any) {
    // eslint-disable-next-line @typescript-eslint/no-unused-expressions
    e.preventDefault;
    //reset animation
    e.target.classList.remove("animate");

    e.target.classList.add("animate");

    e.target.classList.add("animate");

    setTimeout(function () {
      e.target.classList.remove("animate");
    }, 6000);
  };

  var classname = document.getElementsByClassName("button");

  for (var i = 0; i < classname.length; i++) {
    classname[i].addEventListener("click", animateButton, false);
  }

  return <button className="button success col-1">Submit</button>;
}
