# Android Python Synth

Um sintetizador desenvolvido em **Python**, com o objetivo de transformar um celular Android em um instrumento musical portátil.

O projeto será desenvolvido no computador utilizando **VS Code** e **Git/GitHub**, mas a ideia é que o sintetizador possa ser executado posteriormente em um celular Android, como o Samsung A03.

# Objetivo

Criar um sintetizador simples e evolutivo capaz de:

* Gerar áudio em tempo real
* Produzir diferentes formas de onda
* Tocar diferentes notas musicais
* Receber comandos MIDI
* Utilizar um teclado MIDI externo
* Possuir controles de sintetizador
* Funcionar como um instrumento portátil

A ideia final é utilizar um **Akai MPK Mini MK3** conectado ao celular para tocar o sintetizador.

# Estrutura planejada

```text
MPK Mini MK3
     │
     │ USB OTG
     ↓
Android / M12
     │
     ↓
Python Synth
     │
     ↓
Saída de áudio
     │
     ↓
Interface de áudio ou Fone
```

# Tecnologias

## Linguagem

* Python 3

## Desenvolvimento

* Visual Studio Code
* Git
* GitHub

## Processamento de áudio

* NumPy
* Biblioteca de áudio compatível com Android/Python

## MIDI

* MIDI USB
* Akai MPK Mini MK3

## Plataforma

* Windows — desenvolvimento
* Android — execução do sintetizador

# Funcionalidades planejadas

## Osciladores

Inicialmente:

* Sine
* Square
* Sawtooth
* Triangle

## Controles

Planejados:

* Frequência
* Volume
* Attack
* Decay
* Sustain
* Release
* Cutoff
* Resonance
* LFO

## MIDI

O projeto deverá futuramente receber notas através de um controlador MIDI.

Exemplo:

```text
MPK Mini
   ↓
Nota C4
   ↓
Python Synth
   ↓
261.63 Hz
   ↓
Áudio
```

# Android

O desenvolvimento principal será realizado no computador.

Para testar o projeto no celular, poderá ser utilizado o **Termux**, que fornece um ambiente de terminal Linux no Android.

O Termux não é necessário para desenvolver o projeto no PC. Ele será utilizado apenas como uma das formas de executar e testar o código no Android.

# Estrutura do projeto

A estrutura poderá evoluir conforme o desenvolvimento:

```text
python-synth/
│
├── main.py
├── oscillator.py
├── audio.py
├── midi.py
├── envelope.py
├── config.py
│
├── presets/
│
├── requirements.txt
│
└── README.md
```

# Status

**Em desenvolvimento**

## Etapas

* [x] Planejamento
* [ ] Gerar primeira onda senoidal
* [ ] Reproduzir áudio
* [ ] Criar diferentes osciladores
* [ ] Criar sistema de notas
* [ ] Implementar ADSR
* [ ] Implementar MIDI
* [ ] Conectar Akai MPK Mini MK3
* [ ] Criar interface
* [ ] Testar no Android
* [ ] Otimizar latência
* [ ] Criar sistema de presets

# Observação

O projeto está sendo desenvolvido com foco em uso pessoal, buscando criar uma solução portátil que possa servir como alternativa a sintetizadores digitais como o Vital, permitindo utilizar um sintetizador completo sem depender de um computador.

A prioridade é construir o sintetizador gradualmente, entendendo como cada parte funciona, em vez de utilizar um sintetizador pronto.

---

**Projeto pessoal**
