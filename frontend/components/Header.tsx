import styles from './Header.module.scss'

type HeaderProps = {
    title: string,
}

const Header = ({ title }: HeaderProps) => {
    return (
        <header className={styles.header}>
            <h1>{title}</h1>
        </header>
    )
}

export default Header