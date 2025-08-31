#!/usr/bin/env python3
"""
Script para executar todos os testes do projeto
"""
import subprocess
import sys
import os


def run_tests():
    """Executa todos os testes"""
    print("🚀 Executando testes do Dashboard de Vendas")
    print("=" * 50)

    # Verifica se pytest está instalado
    try:
        import pytest
    except ImportError:
        print("❌ pytest não está instalado. Instalando...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements-dev.txt"]
        )

    # Executa os testes
    print("📋 Executando testes unitários...")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/",
            "-v",
            "--cov=.",
            "--cov-report=html",
            "--cov-report=term-missing",
            "--cov-fail-under=90",
        ]
    )

    if result.returncode == 0:
        print("\n✅ Todos os testes passaram!")
        print("📊 Relatório de cobertura gerado em htmlcov/index.html")
    else:
        print("\n❌ Alguns testes falharam!")
        return False

    return True


def run_linting():
    """Executa verificação de código"""
    print("\n🔍 Executando verificação de código...")

    # Verifica se black está instalado
    try:
        import black
    except ImportError:
        print("Instalando black...")
        subprocess.run([sys.executable, "-m", "pip", "install", "black"])

    # Formata o código
    print("🎨 Formatando código com black...")
    subprocess.run(
        [
            sys.executable,
            "-m",
            "black",
            "app.py",
            "database.py",
            "visualizations.py",
            "config.py",
            "tests/",
        ]
    )

    # Verifica se flake8 está instalado
    try:
        import flake8
    except ImportError:
        print("Instalando flake8...")
        subprocess.run([sys.executable, "-m", "pip", "install", "flake8"])

    # Executa linting
    print("🔍 Executando linting com flake8...")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "flake8",
            "app.py",
            "database.py",
            "visualizations.py",
            "config.py",
            "tests/",
        ]
    )

    if result.returncode == 0:
        print("✅ Linting passou!")
    else:
        print("⚠️  Linting encontrou problemas!")


def main():
    """Função principal"""
    print("🚗 Dashboard de Vendas - Testes e Qualidade de Código")
    print("=" * 60)

    # Executa testes
    tests_passed = run_tests()

    # Executa linting
    run_linting()

    print("\n" + "=" * 60)
    if tests_passed:
        print("🎉 Processo concluído com sucesso!")
        print("📊 Verifique o relatório de cobertura em htmlcov/index.html")
    else:
        print("❌ Processo falhou. Verifique os erros acima.")
        sys.exit(1)


if __name__ == "__main__":
    main()
