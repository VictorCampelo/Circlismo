import { useState } from "react";
import { AiOutlineEye, AiOutlineEyeInvisible } from "react-icons/ai";

import { Container } from "./styles";
import { ReactElement } from "react";

interface Input extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  password?: boolean;
  forgetPassword?: boolean;
  error?: boolean;
  textError?: string;
  icon?: ReactElement;
}

export const Input = ({
  label,
  password,
  icon,
  error,
  textError = "",
  ...rest
}: Input) => {
  const [isInputVisible, setIsInputVisible] = useState(true);

  return (
    <Container error={error}>
      <section className="labelContent">
        <label>{label}</label>

        {error && textError && <span>{textError}</span>}
      </section>

      <label className="inputContainter">
        {!!icon && icon}

        <input
          type={password && isInputVisible ? "password" : "text"}
          {...rest}
        />

        {password &&
          (isInputVisible ? (
            <AiOutlineEyeInvisible
              onClick={() => setIsInputVisible(false)}
              size={24}
              color="var(--black-800)"
            />
          ) : (
            <AiOutlineEye
              onClick={() => setIsInputVisible(true)}
              size={24}
              color="var(--black-800)"
            />
          ))}
      </label>
    </Container>
  );
};
