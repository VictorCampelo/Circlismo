import { Container } from "./styles"

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement>{
  title: string;
}

export function Button({ title, ...rest}: ButtonProps) {
  return (
    <Container {...rest}>
      {title}
    </Container>
  )
}