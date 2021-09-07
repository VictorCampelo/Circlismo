import styled from 'styled-components';

export const Container = styled.main`
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 2rem;

  form {
    width: 450px;
    background: var(--white);
    border-radius: 30px;
    box-shadow: 0px 0px 18px -4px #CCCCCC;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0.5rem 2rem 1rem 2rem;

    .title {
      width: 100%;
      margin-bottom: 0.5rem;
      
      h1 {
        font-size: 1.875rem;
        font-weight: 600;
      }

      p {
        font-size: 0.875rem;
        text-align: justify;
        color: var(--gray-300);
        margin-top: 0.5rem;
      }
    }

    .inputContainer {
      display: flex;
      width: 100%;
      flex-direction: column;
      gap: 1rem
    }

    .buttonContainer {
      margin-top: 0.5rem;
    }

    .divisorContainer {
      display: flex;
      width: 100%;
      align-items: center;
      justify-content: center;
      margin-top: 0.5rem;
    }

    .divisor {
      width: 25%;
      height: 1px;
      border-bottom: 1px solid black;
      margin: 0 0.5rem;
    }

    .social {
      width: 45%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 0.5rem;

      svg {
        filter: drop-shadow(0px 3px 3px rgba(0, 0, 0, 0.25));
      }
    }

    .register {
      font-size: 1rem;
      margin-top: 1rem;

      a {
        font-weight: 600;
      }
    }
  }
`