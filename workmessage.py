{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "name": "workmessage.py",
      "toc_visible": true,
      "authorship_tag": "ABX9TyOF/zhjzd0B/v4rG2xlm2+J",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/annenxu/again/blob/main/workmessage.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "exKMGAxSZQca",
        "outputId": "c5b1d265-c866-4312-e9cb-d85012fa6911"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.12/dist-packages (1.51.0)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.3.0)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging<26,>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (25.0)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<13,>=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)\n",
            "Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.5)\n",
            "Requirement already satisfied: pyarrow<22,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.5.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.45)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.9.1)\n",
            "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.5.1)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.1)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.10.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.4.4)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.11)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2025.10.5)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.3)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.4.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.9.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.37.0)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.28.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-11-02 22:58:01.485 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 22:58:01.486 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 22:58:01.487 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 22:58:01.489 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 22:58:01.491 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 22:58:01.492 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 22:58:01.494 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 22:58:01.496 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 22:58:01.498 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 22:58:01.499 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 22:58:01.500 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 22:58:01.501 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 22:58:01.502 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit\n",
        "import streamlit as st\n",
        "import random\n",
        "\n",
        "# Page setup\n",
        "st.set_page_config(page_title=\"Good Luck on Your First Day Pookie\", page_icon=\"🐢\", layout=\"centered\")\n",
        "\n",
        "# Title and description\n",
        "st.title(\"Look at you with a big boy job!\")\n",
        "st.markdown(\"I'm so proud of you and so excited that we're buying Robben Island soon\")\n",
        "\n",
        "# Button to generate a message or display a pre-defined one\n",
        "if st.button(\"Click here, daddy Doerr 🙂‍↕️\"):\n",
        "    # Customize the messages here\n",
        "    messages = [\n",
        "        \"Jokes aside, I am so so so proud of you Niki-poo.\",\n",
        "        \"Good luck on your very first day as a full time office zaddy! I still don't know exactly what you do but those Teams emojis and Excel functions don't know what's coming today. \",\n",
        "        \"You may not want to hear this but know that I'm praying for your joy, success and progression in this role. I believe with my whole heart He'll protect you and strengthen you \",\n",
        "        \"Curtis and I are thinking of you today, and love you a lot! We don't care that you're the office weirdo, we think you're cool ❤️❤️\",\n",
        "    ]\n",
        "    message = random.choice(messages)\n",
        "\n",
        "    # Display the message\n",
        "    st.balloons()\n",
        "    st.success(message)\n",
        "\n",
        "\n",
        "# Write the streamlit app to a file\n",
        "streamlit_code = \"\"\"\n",
        "import streamlit as st\n",
        "import random\n",
        "\n",
        "st.set_page_config(page_title=\"Good Luck on Your First Day Pookie\", page_icon=\"🐢\", layout=\"centered\")\n",
        "\n",
        "\n",
        "st.title(\"Look at you with a big boy job!\")\n",
        "st.markdown(\"I'm so proud of you and so excited that we're buying Robben Island soon\")\n",
        "\n",
        "iif st.button(\"Click here, daddy Doerr 🙂‍↕️\"):\n",
        "\n",
        "    messages = [\n",
        "        \"Jokes aside, I am so so so proud of you Niki-poo.\",\n",
        "        \"Good luck on your very first day as a full time office zaddy! I still don't know exactly what you do but those Teams emojis and Excel functions don't know what's coming today. \",\n",
        "        \"You may not want to hear this but know that I'm praying for your joy, success and progression in this role. I believe with my whole heart He'll protect you and strengthen you \",\n",
        "        \"Curtis and I are thinking of you today, and love you a lot! We don't care that you're the office weirdo, we think you're cool ❤️❤️\",\n",
        "    ]\n",
        "    message = random.choice(messages)\n",
        "\n",
        "\n",
        "    st.balloons()\n",
        "    st.success(message)\n",
        "\"\"\"\n",
        "\n",
        "with open(\"first_day_message_app.py\", \"w\") as f:\n",
        "    f.write(streamlit_code)\n",
        "\n",
        "# You can run this app locally using:\n",
        "# !streamlit run first_day_message_app.py"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e7122c06",
        "outputId": "b841638b-78fa-41c3-9139-4217ff5595b0"
      },
      "source": [
        "%%writefile requirements.txt\n",
        "streamlit"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing requirements.txt\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "83060b38",
        "outputId": "0acfe129-7650-4501-8938-a839b78975ba"
      },
      "source": [
        "!streamlit run first_day_message_app.py"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://136.117.219.170:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "313b1aff",
        "outputId": "9685c7f3-f90a-4c0f-e11c-8bf80e13d28d"
      },
      "source": [
        "!streamlit run isniklucky.py"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.56.135.45:8501\u001b[0m\n",
            "\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9feb4241"
      },
      "source": [
        "# Task\n",
        "Save the Python code from the notebook to a `.py` file and push it to a new GitHub repository."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5d45bad3"
      },
      "source": [
        "## Save the code to a python file\n",
        "\n",
        "### Subtask:\n",
        "Ensure the Python code is saved to a `.py` file in your Colab environment.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0ceaac02"
      },
      "source": [
        "**Reasoning**:\n",
        "The subtask is to save the Python code to a `.py` file. The existing notebook already contains the Python code for the Streamlit app and a `%%writefile` command. I need to execute this command to save the code to the specified file.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "da01f632",
        "outputId": "49456918-b3ca-459b-fea4-cf645e0cfe55"
      },
      "source": [
        "%%writefile first_day_message_app.py\n",
        "import streamlit as st\n",
        "import random\n",
        "\n",
        "st.set_page_config(page_title=\"Good Luck on Your First Day Pookie\", page_icon=\"🐢\", layout=\"centered\")\n",
        "\n",
        "\n",
        "st.title(\"Look at you with a big boy job!\")\n",
        "st.markdown(\"I'm so proud of you and so excited that we're buying Robben Island soon\")\n",
        "\n",
        "if st.button(\"Click here, daddy Doerr 🙂‍↕️\"):\n",
        "\n",
        "    messages = [\n",
        "        \"Jokes aside, I am so so so proud of you Niki-poo.\",\n",
        "        \"Good luck on your very first day as a full time office zaddy! I still don't know exactly what you do but those Teams emojis and Excel functions don't know what's coming today. \",\n",
        "        \"You may not want to hear this but know that I'm praying for your joy, success and progression in this role. I believe with my whole heart He'll protect you and strengthen you \",\n",
        "        \"Curtis and I are thinking of you today, and love you a lot! We don't care that you're the office weirdo, we think you're cool ❤️❤️\",\n",
        "    ]\n",
        "    message = random.choice(messages)\n",
        "\n",
        "\n",
        "    st.balloons()\n",
        "    st.success(message)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting first_day_message_app.py\n"
          ]
        }
      ]
    }
  ]
}