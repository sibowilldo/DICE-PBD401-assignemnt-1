import { callExternalApi } from "@/services/api.service";

const apiServerUrl = `${import.meta.env.VITE_API_SERVER_URL}${import.meta.env.VITE_API_VERSION_FRAGMENT}`;

export const getHome = async (accessToken) => {
    const config = {
        url: `${apiServerUrl}/home`,
        method: "GET",
        headers: {
            "content-type": "application/json",
            Authorization: `Bearer ${accessToken}`,
        },
    };

    const { data, error } = await callExternalApi({ config });

    return {
        data: data || null,
        error,
    };
};

export const getVacancies = async (accessToken) => {
    const config = {
        url: `${apiServerUrl}/vacancies`,
        method: "GET",
        headers: {
            "content-type": "application/json",
            Authorization: `Bearer ${accessToken}`,
        },
    };

    const { data, error } = await callExternalApi({ config });

    return {
        data: data || null,
        error,
    };
};