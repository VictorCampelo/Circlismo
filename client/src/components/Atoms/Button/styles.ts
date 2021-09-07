import styled from 'styled-components';

export const Container = styled.button`
  height: 3.375rem;
  width: auto;
  border: none;
  border-radius: 30px;
  padding: 0 4rem;

  color: var(--white);
  font-weight: 700;
  font-size: 1.125rem;
  background-color: var(--green-confirmation);
  transition: 0.2s background;

  :hover {
    background-color: var(--green-confirmation-darker);
  }

  :disabled{
    background-color: var(--gray-300);
    cursor: not-allowed;
  } 
`